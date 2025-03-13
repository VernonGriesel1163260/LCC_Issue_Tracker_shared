"""
routes.py

This module defines the main routes for the LCC Issue Tracker.
It includes endpoints for login, logout, signup, profile management,
and file upload handling.
"""

from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from ims_app import db, bcrypt, app
from ims_app.controller import validate_login, validate_signup, user_home_url, allowed_mime_type, file_size_valid
from ims_app.models import get_profile_data
from werkzeug.utils import secure_filename
import os

main_bp = Blueprint('main_bp', __name__,
    template_folder='templates',
    static_folder='static')

@main_bp.route('/')
def home():
    """
    Root endpoint.
    
    Redirects the user to the appropriate homepage based on their role.
    """
    return redirect(user_home_url())

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login endpoint.
    
    GET: Render the login page.
    POST: Validate credentials and log in the user, or display error messages.
    
    Returns:
        Redirects to the user's role-specific homepage upon successful login,
        or re-renders the login template with error messages.
    """
    if session.get('loggedin'):
        return redirect(user_home_url())
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        login_state = validate_login(username, password)
        if login_state == 'password_invalid':
            return render_template('login.html', username=username, password_invalid=True)
        elif login_state == 'username_invalid':
            return render_template('login.html', username=username, username_invalid=True)
        elif login_state == 'success':
            return redirect(user_home_url())
    return render_template('login.html')

@main_bp.route('/logout')
def logout():
    """
    Logout endpoint.
    
    Clears the session and redirects to the login page.
    """
    session.clear()
    return redirect(url_for('main_bp.login'))

@main_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Signup (registration) endpoint.
    
    GET: Render the signup page.
    POST: Validate registration details, process profile image upload,
          and create a new user account.
    
    Returns:
        Rendered signup template with either a success message or error messages.
    """
    if session.get('loggedin'):
        return redirect(user_home_url())
    
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        location = request.form.get('location')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validate signup details.
        username_error, email_error, password_error, firstname_error, lastname_error, location_error, confirm_password_error = \
            validate_signup(firstname, lastname, location, username, password, email, confirm_password)
            
        if any([username_error, email_error, password_error, firstname_error, lastname_error, location_error, confirm_password_error]):
            return render_template('signup.html',
                                   firstname=firstname,
                                   lastname=lastname,
                                   location=location,
                                   username=username,
                                   email=email,
                                   username_error=username_error,
                                   email_error=email_error,
                                   password_error=password_error,
                                   firstname_error=firstname_error,
                                   lastname_error=lastname_error,
                                   location_error=location_error,
                                   confirm_password_error=confirm_password_error)
        else:
            # Process profile_image upload
            profile_image_filename = 'images/default.png'
            profile_image_error = None
            if 'profile_image' in request.files:
                file = request.files['profile_image']
                if file.filename != '': #if filename not an empty string
                    if not file_size_valid(file):
                        profile_image_error = "File size must be under 5MB."
                    elif not allowed_mime_type(file):
                        profile_image_error = "Invalid file type. Allowed types: png, jpeg, webp."
                    else:
                        filename = secure_filename(file.filename)
                        upload_folder = os.path.join(app.root_path, 'static', 'images')
                        if not os.path.exists(upload_folder): #only runs if /profile folder not available
                            os.makedirs(upload_folder)
                        file.save(os.path.join(upload_folder, filename))
                        profile_image_filename = filename
                
            # if file was uploaded but it failed validation, re-render with errors
            if profile_image_error is not None:
                return render_template('signup.html',
                                       firstname=firstname,
                                       lastname=lastname,
                                       location=location,
                                       username=username,
                                       email=email,
                                       username_error=username_error,
                                       email_error=email_error,
                                       password_error=password_error,
                                       firstname_error=firstname_error,
                                       lastname_error=lastname_error,
                                       location_error=location_error,
                                       profile_image_error=profile_image_error,
                                       confirm_password_error=confirm_password_error)
            
            password_hash = bcrypt.generate_password_hash(password)
            with db.get_cursor() as cursor:
                cursor.execute('''
                    INSERT INTO users (username, password_hash, email, first_name, last_name, location, role, profile_image)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                ''', (username, password_hash, email, firstname, lastname, location, 'visitor', profile_image_filename))
            return render_template('signup.html', signup_successful=True)
    return render_template('signup.html')


@main_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    """
    Profile endpoint for viewing and updating the current user's profile.
    
    GET: Retrieves the user's profile from the database and renders the profile template.
    POST: Validates and updates the user's profile data (including password change if provided).
    
    Returns:
        Rendered profile template with updated information and success or error messages.
    """
    if not session.get('loggedin'):
        return redirect(url_for('main_bp.login'))
    
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('main_bp.login'))
    
    if request.method == 'GET':
        profile_data = get_profile_data()
        return render_template('profile.html', profile=profile_data)
    
    elif request.method == 'POST':
        username = request.form.get('username')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        location = request.form.get('location')
        new_password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validate the updated details
        username_error, email_error, password_error, firstname_error, lastname_error, location_error, confirm_password_error = \
            validate_signup(firstname=firstname, lastname=lastname, location=location, username=username, 
                            password=new_password if new_password else "validplaceholder", 
                            email=email, confirm_password=confirm_password if new_password else "validplaceholder")
        pass
        # Check if new password provided and if they match
        if new_password and new_password != confirm_password:
            confirm_password_error = "Passwords do not match"
        
        if any([email_error, (password_error if new_password else None), firstname_error, lastname_error, location_error, confirm_password_error]):
            # Re-render the template with error messages
            return render_template('profile.html', 
                                   profile={
                                       'first_name': firstname,
                                       'last_name': lastname,
                                       'email': email,
                                       'location': location,
                                       'username': username,
                                       'profile_image': get_profile_data().get('profile_image', 'default.png')
                                   },
                                   username_error=username_error,
                                   email_error=email_error,
                                   password_error=password_error,
                                   firstname_error=firstname_error,
                                   lastname_error=lastname_error,
                                   location_error=location_error,
                                   confirm_password_error=confirm_password_error)
        
        # Update the database
        with db.get_cursor() as cursor:
            if new_password:
                new_password_hash = bcrypt.generate_password_hash(new_password)
                cursor.execute('''
                    UPDATE users
                    SET first_name = %s,
                        last_name = %s,
                        email = %s,
                        location = %s,
                        password_hash = %s
                    WHERE user_id = %s;
                ''', (firstname, lastname, email, location, new_password_hash, user_id))
            else:
                cursor.execute('''
                    UPDATE users
                    SET first_name = %s,
                        last_name = %s,
                        email = %s,
                        location = %s
                    WHERE user_id = %s;
                ''', (firstname, lastname, email, location, user_id))
        
        # Re-fetch updated profile data and render with a success message.
        profile_data = get_profile_data()
        return render_template('profile.html', profile=profile_data, update_success="Profile updated successfully.")

@main_bp.route('/profile/remove_image', methods=['POST'])
def remove_profile_image():
    """
    Remove the current user's profile image from the server and set it to default.
    
    Returns:
        A redirect to the profile page with a flash message indicating the result.
    """
    if not session.get('loggedin'):
        return redirect(url_for('main_bp.login'))
    
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('main_bp.login'))
    
    profile = get_profile_data()
    current_image = profile.get('profile_image', 'default.png')
    
    # Prevent static removal if profile image already default
    if current_image == 'default.png' or current_image.endswith('default.png'):
        return redirect(url_for('main_bp.profile'))
    
    # Construct file path; images are stored in static/images/
    image_path = os.path.join(app.root_path, 'static', 'images', current_image)
    if os.path.exists(image_path):
        try:
            os.remove(image_path)
        except Exception as e:
            flash("Could not remove image.", "danger")

    # Update the user's profile image to default in the database
    with db.get_cursor() as cursor:
        cursor.execute('''UPDATE users 
                       SET profile_image = %s 
                       WHERE user_id = %s
                       ''', ('default.png', user_id))
        
    flash("Profile image removed successfully.", "success")
    return redirect(url_for('main_bp.profile'))

@main_bp.route('/profile/change_image', methods=['POST'])
def change_profile_image():
    """
    Change the current user's profile image.
    
    Validates the uploaded file's size and MIME type. If valid, removes the old image
    (if not default) and updates the user's profile with the new image filename.
    
    Returns:
        A redirect to the profile page with a flash message indicating the result.
    """
    if not session.get('loggedin'):
        return redirect(url_for('main_bp.login'))
    
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('main_bp.login'))
    
    if 'profile_image' not in request.files:
        return redirect(url_for('main_bp.profile'))
    
    file = request.files['profile_image']
    if file.filename == '':
        flash("No file chosen", "danger")
        return redirect(url_for('main_bp.profile'))
    
    # Validate file size and MIME type
    if not file_size_valid(file):
        flash("File size must be under 5MB.", "danger")
        return redirect(url_for('main_bp.profile'))
    if not allowed_mime_type(file):
        flash("Invalid file type. Allowed types: png, jpeg, webp.", "danger")
        return redirect(url_for('main_bp.profile'))
    
    # Remove previous image if it is not the default
    profile = get_profile_data()
    current_image = profile.get('profile_image', 'default.png')
    if current_image != 'default.png' and not current_image.endswith('default.png'):
        old_image_path = os.path.join(app.root_path, 'static', 'images', current_image)
        if os.path.exists(old_image_path):
            try:
                os.remove(old_image_path)
            except Exception as e:
                flash("Could not upload image.", "danger")
                pass
    
    # Save new file
    filename = secure_filename(file.filename)
    upload_folder = os.path.join(app.root_path, 'static', 'images')
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    file.save(os.path.join(upload_folder, filename))
    
    # Update database with the new filename
    with db.get_cursor() as cursor:
        cursor.execute('''UPDATE users 
                       SET profile_image = %s 
                       WHERE user_id = %s
                       ''', (filename, user_id))
        
    flash("Profile image changed successfully.", "success")
    return redirect(url_for('main_bp.profile'))