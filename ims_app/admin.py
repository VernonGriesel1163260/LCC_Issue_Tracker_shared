"""
admin.py

This module defines the Blueprint for admin user management functionality.
It provides endpoints for:
  - Listing users (with search)
  - Updating a user's status
  - Updating a user's role
  - Viewing any user's profile

Only users with the admin role are allowed access to these endpoints.
"""

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from ims_app import db

admin_bp = Blueprint('admin_bp', __name__,
                       template_folder='templates',
                       static_folder='static')

def admin_required():
    """
    Check if the current user is an admin.

    Returns:
        True if the user role is 'admin'; otherwise, False.
    """
    return session.get('role') == 'admin'

@admin_bp.route('/admin/users', methods=['GET'])
def list_users():
    """
    Display a list of users with search functionality.
    
    Admins can search by username, first name, or last name.
    
    Returns:
        Rendered template (admin_users.html) with a list of users.
    """
    if not admin_required():
        # flash("Access denied.", "danger")
        return render_template('access_denied.html')
    
    search = request.args.get('search', '').strip()
    query = """
        SELECT user_id, username, first_name, last_name, email, role, status, profile_image
        FROM users
    """
    params = []
    if search:
        query += " WHERE username LIKE %s OR first_name LIKE %s OR last_name LIKE %s"
        like_search = f"%{search}%"
        params.extend([like_search, like_search, like_search])
    query += " ORDER BY username"
    
    with db.get_cursor() as cursor:
        cursor.execute(query, tuple(params))
        users = cursor.fetchall()
    
    return render_template('admin_users.html', users=users, search=search)

@admin_bp.route('/admin/users/update_status', methods=['POST'])
def update_user_status():
    """
    Update the status of a user.
    
    Only admins are allowed to update a user's status.
    
    Returns:
        A redirect to the user management page with a flash message.
    """
    if not admin_required():
        # flash("Access denied.", "danger")
        return render_template('access_denied.html')
    
    user_id = request.form.get('user_id')
    new_status = request.form.get('status')
    # Ensure status is one of the allowed values.
    if new_status not in ['active', 'inactive']:
        flash("Invalid status value.", "danger")
        return redirect(url_for('admin_bp.list_users'))
    
    with db.get_cursor() as cursor:
        cursor.execute('''UPDATE users 
                       SET status = %s 
                       WHERE user_id = %s
                       ''', (new_status, user_id))
    
    flash("User status updated successfully.", "success")
    return redirect(url_for('admin_bp.list_users'))

@admin_bp.route('/admin/users/update_role', methods=['POST'])
def update_user_role():
    """
    Update the role of a user.
    
    Only admins are allowed to update a user's role.
    
    Returns:
        A redirect to the user management page with a flash message.
    """
    if not session.get('role') == 'admin':
        flash("Access denied.", "danger")
        return redirect(url_for('main_bp.login'))
    
    user_id = request.form.get('user_id')
    new_role = request.form.get('role')
    if new_role not in ['visitor', 'helper', 'admin']:
        flash("Invalid role value.", "danger")
        return redirect(url_for('admin_bp.list_users'))
    
    with db.get_cursor() as cursor:
        cursor.execute("UPDATE users SET role = %s WHERE user_id = %s", (new_role, user_id))
    
    flash("User role updated successfully.", "success")
    return redirect(url_for('admin_bp.list_users'))


@admin_bp.route('/admin/user/<int:user_id>', methods=['GET'])
def view_user_profile(user_id):
    """
    View the profile of a specific user.
    
    Only admins are allowed to view any user's profile.
    
    Args:
        user_id (int): The ID of the user whose profile is to be viewed.
    
    Returns:
        Rendered template (admin_user_profile.html) with the user's profile data,
        or a redirect with an error message if the user is not found.
    """
    if not admin_required():
        # flash("Access denied.", "danger")
        return render_template('access_denied.html')
    
    with db.get_cursor() as cursor:
        cursor.execute('''
            SELECT user_id, username, first_name, last_name, email, role, status, profile_image, location 
            FROM users 
            WHERE user_id = %s
        ''', (user_id,))
        user_profile = cursor.fetchone()
    
    if not user_profile:
        flash("User not found.", "danger")
        return redirect(url_for('admin_bp.list_users'))
    
    return render_template('admin_user_profile.html', user_profile=user_profile)
