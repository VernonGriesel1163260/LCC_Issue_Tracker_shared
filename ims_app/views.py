"""
views.py

This module defines the Blueprint for rendering role-specific home pages and error pages.
It includes endpoints for visitors, helpers, and admins, ensuring that only users with the
correct role can access their respective home pages.
"""
from flask import Blueprint, render_template, redirect, url_for, session

views_bp = Blueprint('views_bp', __name__,
    template_folder='templates',
    static_folder='static')

@views_bp.route('/visitor/home')
def home_visitor():
    """
    Render the home page for visitors.
    
    Returns:
        Rendered template for visitor home if the user is logged in as a visitor;
        otherwise, redirects to the login page or shows an access denied message.
    """
    if not session.get('loggedin'):
        return redirect(url_for('main_bp.login'))
    if not session.get('role') == 'visitor':
        return render_template('access_denied.html')
    return render_template('home_visitor.html')

@views_bp.route('/helper/home')
def home_helper():
    """
    Render the home page for helpers.
    
    Returns:
        Rendered template for helper home if the user is logged in as a helper;
        otherwise, redirects to the login page or shows an access denied message.
    """
    if not session.get('loggedin'):
        return redirect(url_for('main_bp.login'))
    if not session.get('role') == 'helper':
        return render_template('access_denied.html')
    return render_template('home_helper.html')

@views_bp.route('/admin/home')
def home_admin():
    """
    Render the home page for administrators.
    
    Returns:
        Rendered template for admin home if the user is logged in as an admin;
        otherwise, redirects to the login page or shows an access denied message.
    """
    if not session.get('loggedin'):
        return redirect(url_for('main_bp.login'))
    if not session.get('role') == 'admin':
        return render_template('access_denied.html')
    return render_template('home_admin.html')
            
@views_bp.route('/404')
def page_not_found():
    """
    Render the access denied page.
    
    Returns:
        Rendered template for access denied.
    """
    return render_template('access_denied.html')