"""
issues.py

This module defines the Blueprint for issue reporting and management for the LCC Issue Tracker.
It includes endpoints for:
  - Listing issues (only unresolved issues for visitors, all unresolved for helpers/admins)
  - Reporting a new issue
  - Viewing issue details along with comments
  - Adding comments to issues (with automatic status update for helpers/admins)
  - Listing resolved issues in a separate view
"""
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from ims_app import db

issues_bp = Blueprint('issues_bp', __name__,
                        template_folder='templates',
                        static_folder='static')

def fetch_comments(issue_id):
    """
    Helper function to fetch comments for a given issue.
    
    Args:
        issue_id (int): The ID of the issue.
    
    Returns:
        A list of dictionaries, each representing a comment.
    """
    with db.get_cursor() as cursor:
        cursor.execute('''
            SELECT c.*, u.username, u.profile_image, u.role 
            FROM comments c 
            JOIN users u ON c.user_id = u.user_id 
            WHERE c.issue_id = %s 
            ORDER BY c.created_at ASC
        ''', (issue_id,))
        return cursor.fetchall()

@issues_bp.route('/issues', methods=['GET'])
def list_issues():
    """
    List unresolved issues for the logged-in user.
    
    - Visitors see only their own issues.
    - Helpers and Admins see all issues except those marked as 'resolved'.
    
    Returns:
        Rendered template (issues_list.html) with a list of issues and their comments.
    """
    role = session.get('role')
    user_id = session.get('user_id')
    with db.get_cursor() as cursor:
        if role == 'visitor':
            cursor.execute(
                '''SELECT * 
                FROM issues 
                WHERE user_id = %s AND status <> 'resolved' 
                ORDER BY created_at DESC''', 
                (user_id,)
            )
        else:
            cursor.execute(
                '''SELECT * 
                FROM issues 
                WHERE status <> 'resolved' 
                ORDER BY created_at DESC'''
            )
        issues = cursor.fetchall()

    # For each issue, get comments (using a separate query for clarity).
    for issue in issues:
        issue['comments'] = fetch_comments(issue['issue_id'])
    
    return render_template('issues_list.html', issues=issues)

@issues_bp.route('/issues/new', methods=['GET', 'POST'])
def new_issue():
    """
    Endpoint to report a new issue.
    
    GET: Renders the new_issue template.
    POST: Inserts a new issue into the database and redirects to the issues list.
    
    Returns:
        Rendered template (new_issue.html) or a redirect.
    """
    if not session.get('loggedin'):
        return redirect(url_for('main_bp.login'))
    
    if request.method == 'POST':
        summary = request.form.get('summary')
        description = request.form.get('description')
        user_id = session.get('user_id')
        
        if not summary or not description:
            flash("Please provide both a summary and a description.", "danger")
            return redirect(url_for('issues_bp.new_issue'))
        
        with db.get_cursor() as cursor:
            cursor.execute('''
                INSERT INTO issues (user_id, summary, description, status, created_at)
                VALUES (%s, %s, %s, %s, NOW())
            ''', (user_id, summary, description, 'new'))
        flash("Issue reported successfully.", "success")
        return redirect(url_for('issues_bp.list_issues'))
    
    return render_template('new_issue.html')

@issues_bp.route('/issues/<int:issue_id>', methods=['GET', 'POST'])
def issue_detail(issue_id):
    """
    Display the details of a specific issue and allow users to add comments.
    
    GET: Retrieves the issue and its comments, and renders the issue_detail template.
    POST: Inserts a new comment. For helpers/admins, also sets the issue status to "open" if applicable.
    
    Args:
        issue_id (int): The ID of the issue.
    
    Returns:
        Rendered template (issue_detail.html) or a redirect.
    """
    if not session.get('loggedin'):
        return redirect(url_for('main_bp.login'))
    
    role = session.get('role')
    user_id = session.get('user_id')
    
    with db.get_cursor() as cursor:
        cursor.execute("SELECT * FROM issues WHERE issue_id = %s", (issue_id,))
        issue = cursor.fetchone()
    
    if not issue:
        flash("Issue not found.", "danger")
        return redirect(url_for('issues_bp.list_issues'))
    
    # visitors can only view their own issues
    if role == 'visitor' and issue['user_id'] != user_id:
        flash("Access denied. You can only view your own issues.", "danger")
        return redirect(url_for('issues_bp.list_issues'))
    
    if request.method == 'POST':
        # Process adding a new comment.
        content = request.form.get('content')
        if not content:
            flash("Comment cannot be empty.", "danger")
        else:
            with db.get_cursor() as cursor:
                cursor.execute('''
                    INSERT INTO comments (issue_id, user_id, content, created_at)
                    VALUES (%s, %s, %s, NOW())
                ''', (issue_id, user_id, content))
            flash("Comment added successfully.", "success")

            
            # If the commenter is a helper or admin, update issue status to "open"
            if role in ['helper', 'admin'] and issue['status'] in ['new', 'stalled', 'resolved']:
                with db.get_cursor() as cursor:
                    cursor.execute("UPDATE issues SET status = 'open' WHERE issue_id = %s", (issue_id,))
                flash("Issue status updated to open.", "info")
        return redirect(url_for('issues_bp.issue_detail', issue_id=issue_id))
    
    # Fetch comments for the issue.
    comments = fetch_comments(issue['issue_id'])
    
    return render_template('issue_detail.html', issue=issue, comments=comments)

@issues_bp.route('/issues/resolved', methods=['GET'])
def list_resolved_issues():
    """
    List resolved issues.
    
    - Visitors see only their own resolved issues.
    - Helpers and Admins see all resolved issues.
    
    Returns:
        Rendered template (issues_resolved.html) with a list of resolved issues and their comments.
    """
    if not session.get('loggedin'):
        return redirect(url_for('main_bp.login'))
    
    role = session.get('role')
    user_id = session.get('user_id')
    
    with db.get_cursor() as cursor:
        if role == 'visitor':
            cursor.execute('''SELECT * 
                           FROM issues 
                           WHERE user_id = %s AND status = 'resolved' 
                           ORDER BY created_at DESC
                           ''', (user_id,))
        else:
            cursor.execute("SELECT * FROM issues WHERE status = 'resolved' ORDER BY created_at DESC")
        issues = cursor.fetchall()
    
    for issue in issues:
        with db.get_cursor() as cursor:
            cursor.execute('''
                SELECT c.*, u.username, u.profile_image, u.role 
                FROM comments c 
                JOIN users u ON c.user_id = u.user_id 
                WHERE c.issue_id = %s 
                ORDER BY c.created_at ASC
            ''', (issue['issue_id'],))
            issue['comments'] = cursor.fetchall()
    
    return render_template('issues_resolved.html', issues=issues)

@issues_bp.route('/issues/<int:issue_id>/update_status', methods=['POST'])
def update_issue_status(issue_id):
    """
    Update the status of an issue.
    
    Only helpers and admins are authorized to update an issue's status.
    After updating, redirects the user to the originating page using the 'next' parameter,
    or falls back to the referrer.
    
    Args:
        issue_id (int): The ID of the issue to update.
    
    Returns:
        A redirect to the originating page.
    """
    if session.get('role') not in ['helper', 'admin']:
        flash("You are not authorized to update issue status.", "danger")
        return redirect(url_for('issues_bp.list_issues'))
    
    new_status = request.form.get('status')
    if new_status not in ['new', 'open', 'stalled', 'resolved']:
        flash("Invalid status.", "danger")
        return redirect(url_for('issues_bp.list_issues'))
    
    with db.get_cursor() as cursor:
        cursor.execute('''UPDATE issues 
                       SET status = %s 
                       WHERE issue_id = %s
                       ''', (new_status, issue_id))
    flash("Issue status updated.", "success")

    # Get the 'next' URL from the form or fallback to the referrer
    next_url = request.form.get('next') or request.referrer or url_for('issues_bp.list_issues')
    return redirect(next_url)