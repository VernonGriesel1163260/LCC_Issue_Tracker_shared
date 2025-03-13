"""
index.py

This module defines the root endpoints for the LCC Issue Tracker.
It includes the root URL ("/"), login, signup, and logout endpoints,
delegating authentication and redirection logic to the appropriate functions
and blueprints.
"""

from flask import redirect, Blueprint, render_template, request, session, url_for
from ims_app import app, db, bcrypt, user_bp
from ims_app import controller
from ims_app.controller import validate_login, validate_signup

# Default role assigned to new users upon registration.
DEFAULT_USER_ROLE = 'visitor'

@app.route('/')
def home():
    """
    Root endpoint that redirects users based on their login status and role.
    
    Returns:
        Redirect to the role-specific homepage if logged in, otherwise to login page.
    """
    return redirect(controller.user_home_url())

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle user login.
    
    GET: Render the login page.
    POST: Validate credentials and log the user in, or display errors.
    
    Returns:
        Redirect to role-specific homepage on success, or re-render login page on failure.
    """
    
    if 'loggedin' in session:
        return redirect(controller.user_home_url())
    
    
    if request.method=='POST' and 'username' in request.form and 'password' in request.form:
        # Get the login details submitted by the user.
        username = request.form['username']
        password = request.form['password']
        
        login_state = validate_login(username,password)
        
        if login_state == 'password_invalid':
            return render_template('login.html', username=username, password_invalid=True)
        elif login_state == 'username_invalid':
            return render_template('login.html', username=username, username_invalid=True)
        elif login_state == 'success':
            return redirect(controller.user_home_url())
        else:
            pass
    
    # This was a GET request, or an invalid POST (no username and/or password),
    # so we just render the login form with no pre-populated details or flags.
    return render_template('login.html')

@user_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Handle new user registration.
    
    GET: Render the signup page.
    POST: Validate input and create a new account, or re-render with errors.
    
    Returns:
        Rendered signup page with a success message or error messages.
    """
    if 'loggedin' in session:
         return redirect(controller.user_home_url())
    
    if request.method == 'POST' and 'username' in request.form and 'email' in request.form and 'password' in request.form:
        # Get the details submitted via the form on the signup page, and store
        # the values in temporary local variables for ease of access.
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        location = request.form['location']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # We start by assuming that everything is okay. If we encounter any
        # errors during validation, we'll store an error message in one or more
        # of these variables so we can pass them through to the template.
        username_error = None
        email_error = None
        password_error = None
        firstname_error = None
        lastname_error = None
        location_error = None
        
        username_error, email_error, password_error, firstname_error, lastname_error, location_error = validate_signup(firstname, lastname, location, username, password, email)

        if (username_error or email_error or password_error or firstname_error or lastname_error or location_error):
            # One or more errors were encountered, so send the user back to the
            # signup page with their username and email address pre-populated.
            # For security reasons, we never send back the password they chose.
            return render_template('signup.html',
                                   firstname=firstname,
                                   lastname=lastname,
                                   location=location,
                                   username=username,
                                   email=email,
                                   username_error=username_error,
                                   email_error=email_error,
                                   password_error=password_error,
                                   firstname_error = firstname_error,
                                   lastname_error = lastname_error,
                                   location_error = location_error)
        else:
            # The new account details are valid. Hash the user's new password
            # and create their account in the database.
            password_hash = bcrypt.generate_password_hash(password)
            
            # Note: In this example, we just assume the SQL INSERT statement
            # below will run successfully. But what if it doesn't?
            #
            # If the INSERT fails for any reason, MySQL Connector will throw an
            # exception and the user will receive a generic error page. We
            # should implement our own error handling here to deal with that
            # possibility, and display a more useful message to the user.
            with db.get_cursor() as cursor:
                cursor.execute('''
                               INSERT INTO users (username, password_hash, email, first_name, last_name, location, role, profile_image)
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                               ''',
                               (username, password_hash, email, firstname, lastname, location, DEFAULT_USER_ROLE,'default.png'))
            
            # Now that registration is complete, send the user back to the
            # signup page. We set the `signup_successful` flag to display a
            # post-signup message.
            return render_template('signup.html', signup_successful=True)            

    # This was a GET request, or an invalid POST (no username, email, and/or
    # password). Render the signup page with no pre-populated form fields or
    # error messages.
    return render_template('signup.html')

@user_bp.route('/logout')
def logout():
    """
    Log out the current user by clearing the session.
    
    Returns:
        Redirect to the login page.
    """
    # session.pop('loggedin', None)
    # session.pop('user_id', None)
    # session.pop('username', None)
    # session.pop('role', None)
    session.clear()
    
    return redirect(url_for('user_bp.login'))



app.register_blueprint(user_bp)