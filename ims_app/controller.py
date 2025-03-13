"""_summary_

Returns:
    _type_: _description_
"""

from flask import Blueprint, session, url_for
import re
import os
from ims_app import db, bcrypt
from ims_app.models import get_profile_data
import magic # extensions could be an easy and cheap way to validate files, but I've used the magic module before.

# TODO create a blueprint to include additional auth routes.
controller_bp = Blueprint('controller_bp', __name__,
    template_folder='templates',
    static_folder='static')

def user_home_url():
    role = session.get('role')
    if role == 'visitor':
        return url_for('views_bp.home_visitor')
    elif role == 'helper':
        return url_for('views_bp.home_helper')
    elif role == 'admin':
        return url_for('views_bp.home_admin')
    else:
        return url_for('main_bp.login')

def validate_login(username='', password=''):
    with db.get_cursor() as cursor:
        cursor.execute('''
            SELECT user_id, username, password_hash, role
            FROM users
            WHERE username = %s;
        ''', (username,))
        account = cursor.fetchone()
        if account is not None:
            if bcrypt.check_password_hash(account['password_hash'], password):
                session['loggedin'] = True
                session['user_id'] = account['user_id']
                session['username'] = account['username']
                session['role'] = account['role']
                return 'success'
            else:
                return 'password_invalid'
        else:
            return 'username_invalid'

def validate_signup(firstname=None, lastname=None, location=None, username=None, password=None, email=None, confirm_password=None):
    username_error = email_error = password_error = firstname_error = lastname_error = location_error = confirm_password_error = None
    
    if len(firstname) > 50:
        firstname_error = 'Your first name cannot exceed 50 characters.'
    elif not re.match(r"^[A-Za-z]+[A-Za-z '\-]*[A-Za-z]+$", firstname):
        firstname_error = 'Your first name can only contain letters.'

    if len(lastname) > 50:
        lastname_error = 'Your last name cannot exceed 50 characters.'
    elif not re.match(r"^[A-Za-z]+[A-Za-z '\-]*[A-Za-z]+$", lastname):
        lastname_error = 'Your last name can only contain letters.'

    if len(location) > 100:
        location_error = 'Your location cannot exceed 100 characters.'
    elif not re.match(r'^[\w\s,.\'-()]+$', location):
        location_error = 'Your location can NOT contain special characters.'

    with db.get_cursor() as cursor:
        cursor.execute('SELECT user_id FROM users WHERE username = %s;', (username,))
        if cursor.fetchone():
            username_error = 'An account already exists with this username.'
    if len(username) > 20:
        username_error = 'Your username cannot exceed 20 characters.'
    elif not re.match(r'^[A-Za-z0-9]+$', username):
        username_error = 'Your username can only contain letters and numbers.'

    if len(email) > 320:
        email_error = 'Your email address cannot exceed 320 characters.'
    elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        email_error = 'Invalid email address.'

    # very simple implementation to validate passwords. More rules can be added to make the passwords more secure.
    if session.get('loggedin'):
        # Retrieve the current password hash from the user's profile
        profile = get_profile_data()  # This returns a dictionary including 'password_hash'
        current_hash = profile.get('password_hash')
    
    if len(password) < 8:
        password_error = 'Password length must be at least 8 characters'
    elif not re.search(r'[\d]', password):
        password_error = 'Your password must contain at least one special character, one number, one letter.'
    elif not re.search(r'[a-zA-Z]', password):
        password_error = 'Your password must contain at least one special character, one number, one letter.'
    elif not re.search(r'[^a-zA-Z0-9]', password):
        password_error = 'Your password must contain at least one special character, one number, one letter.'
    elif session.get('loggedin') and bcrypt.check_password_hash(current_hash, password):
        password_error = "New password must be different from your old password."
        
    if password != confirm_password:
        confirm_password_error = 'Passwords do not match'
        
    return username_error, email_error, password_error, firstname_error, lastname_error, location_error, confirm_password_error

def allowed_mime_type(file):
    """uses python-magic module to read the header of the file in the form
        if there is a MIME type.

    Args:
        file (ImmutableMultiDict[str, FileStorage]): immutable file storage dictionary from werkzeug module

    Returns:
        Boolean: True/False
    """
    try:
        mime = magic.from_buffer(file.stream.read(2048), mime=True)
        file.stream.seek(0)  # Reset file pointer after reading
    except  Exception as e:
        mime = False

    return mime in ['image/png', 'image/jpeg', 'image/webp']

def file_size_valid(file, max_size=5*1024*1024):
    """If content_length is available, read that, otherwise seek to the end of the file and compare to max size
        and if those fail. Assume file is unreadable.

    Args:
        file (ImmutableMultiDict[str, FileStorage]): _description_
        max_size (integer, optional): Maximum allowable file size. Defaults to 5*1024*1024 (5MB).

    Returns:
        Boolean: True or False
    """
    try:
        # use the provided content_length if available
        if file.content_length is not None:
            return file.content_length <= max_size
        
        file.stream.seek(0, os.SEEK_END)
        size = file.stream.tell()
        file.stream.seek(0)  # Reset pointer for subsequent reads
        return size <= max_size
    except Exception as e:
        return False
