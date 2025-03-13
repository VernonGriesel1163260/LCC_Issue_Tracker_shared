# LCC_Issue_Tracker
Issue Management System for Lincoln Community Campground (LCC)

## Student Details
**Student Name**: Vernon Griesel  
**Student ID**: 1163260  

## Table of Contents
- [Introduction](#introduction)
- [Features](#features-of-project)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Local Setup](#local-setup)
  - [Database Setup](#database-setup)
  - [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Deployment on PythonAnywhere](#deployment-on-pythonanywhere)
- [Usage](#usage)
- [References & Credits](#references--credits)

## Introduction
The **LCC Issue Tracker** is a web application developed using Python and Flask to help manage issues at Lincoln Community Campground.  
This system allows visitors, helpers, and administrators to:
- Register and log in securely.
- Report new issues with a brief summary and detailed description.
- View, comment on, and update the status of reported issues.
- Manage user profiles and images.
- Admins can manage users, change roles, and update statuses.

## Features of project
- **User Authentication**: Secure registration, login, and logout with hashed passwords.
- **Role-Based Access Control**: Different access levels for visitors, helpers, and administrators.
- **Issue Reporting**: Users can report issues and view only their own issues (visitors) or all issues (helpers/admins).
- **Commenting and Status Updates**: Comments can be added to issues with automatic status changes for helpers/admins.
- **Profile Management**: View and update profile details and profile images.
- **Responsive Design**: Bootstrap-based layout.
- **Campground Theme**: Consistent styling using #585c33 throughout the UI.

## Technology Stack
- **Backend**: Python, Flask, MySQL (via mysql-connector-python)
- **Frontend**: HTML, CSS, Bootstrap
- **Security**: Flask-Bcrypt for password hashing, Flask sessions for authentication (client-side only)
- **Deployment**: Designed for local development and PythonAnywhere hosting

## Project Structure
```bash
LCC_Issue_Tracker/
├── ims_app/
│ ├── init.py # Initializes the Flask app, blueprints, and error handlers
│ ├── admin.py # Admin-specific routes for user management
│ ├── connect.py # Defines the MySQL database connection details for this app. (Ignored by Git)
│ ├── db.py # Implements simple MySQL database connectivity for a Flask web app.
│ ├── controller.py # Logic and helper functions for authentication and routing
│ ├── index.py # Defines the root endpoints for the LCC Issue Tracker
│ ├── issues.py # Routes for reporting, viewing, and commenting on issues
│ ├── models.py # Data access functions (e.g., get_profile_data)
│ ├── routes.py # Main routes for login, signup, profile, file uploads, etc.
│ └── views.py # Role-specific routes
├── templates/ # HTML templates for the web app
│ ├── _base.html # base template for pages seen by a logged-in user, and provides the top-level menus
│ ├── access_denied.html # Error page to use when a user tries to access a page, they're not to enter
│ ├── admin_user_profile.html # Lists the user profiles for administrators
│ ├── admin_users.html # Opens the selected user profile for administrators
│ ├── home_admin.html # Admin Specific Cards
│ ├── home_helper.html # Helper Specific Cards
│ ├── home_visitor.html # Visitor Specific Cards (none at the moment)
│ ├── home # top-level home cards for all registered users
│ ├── issue_detail.html # Displays issue details and can add comments
│ ├── issues_list.html # Lists all (unresolved) issues applicable to 'role'
│ ├── issues_resolved.html # Lists all resolved issues applicable to 'role'
│ ├── login.html # login page
│ ├── new_issues.html # Page to log new issues
│ ├── placeholder.html # used only as a development page for testing
│ ├── profile.html  # User profile pages as applicable to role
│ └── signup.html # Registration page for signing up new account
├── static/
│ └── images/ # Stores profile images and other static images
├── run.py # Entry point for running the application locally
├── requirements.txt # List of required Python packages
├── README.md # Project documentation
├── dbERD_LCC_Issue_Tracker.mwb # ERD model for App database
├── password_hash_generator.py # Script to generate password hashes for one or more user accounts.
├── create_database_local.sql # SQL script for database creation (locally)
├── populate_database_local.sql # SQL script for populating the database with test data (locally)
├── reset_database_local.sql # SQL script for database creation (locally)
├── create_database_pa.sql # SQL script for database creation (PythonAnywhere)
├── populate_database_pa.sql # SQL script for populating the database with test data (PythonAnywhere)
└── reset_database_pa.sql # SQL script for database creation (PythonAnywhere)
```
## Setup Instructions

### Local Setup
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/YourUsername/LCC_Issue_Tracker.git
   cd LCC_Issue_Tracker
   ```

2. **Create a Virtual Environment**  
    ```bash
    python -m venv .venv
    ```
   - Activate the environment on Windows:
    ```bash
    .venv\Scripts\activate
    ```
   - Activate the environment on macOS/Linux:
    ```bash
    source .venv/bin/activate
    ```

3. **Install Dependencies**
   ```python
   pip install -r requirements.txt
   ```

## Database Setup
_local is for running locally. _pa is for running the scripts on python anywhere, you may need to change the username$database_name in the script files
<br>The test data was created using AI, but the scripts were reverse engineered and hand typed.
1. Create the Database
>Use your MySQL client (or MySQL Workbench) to run the provided **create_database.sql** script to create the database and tables.
2. Populate the Database
>Run the **populate_database.sql** script to insert initial test data.
3. (optionally) Reset Database
>Run the **reset_database.sql** script to delete database and populate (create + populate).

## Configuration
- Database Credentials
    <br>Update the ims_app/connect.py file with your local MySQL credentials.
    <br>Note: This file is excluded from GitHub.
    For your local MySQL instance:
    - Username (`dbuser`), Host (`dbhost`), and Port (`dbport`) can be found on the
        MySQL Workbench home screen.
    - Password (`dbpass`) is whatever you set up during installation.
    - Database name (`dbname`) is the name of the database you created for this app.
    - Example connect.py: 
    ```python
    dbuser = 'root' # PUT YOUR USERNAME HERE - usually "root"
    dbpass = 'password'  # PUT YOUR PASSWORD HERE
    dbhost = 'localhost'
    dbport = '3306'
    dbname = 'LCC_Issue_Tracker_db'
    ```

    On PythonAnywhere:
    - Username (`dbuser`) and Host (`dbhost`) are shown on the Databases tab.
    - Port (`dbport`) is 3306 (the default MySQL port).
    - Password (`dbpass`) is whatever you chose in the "MySQL password" section of
        the Databases tab. You can't see what the current password is, so if you've
        forgotten it you'll need to set a new one.
    - Database name (`dbname`) is the name of the database you created for this app
        on PythonAnywhere. It will be listed in the "Your databases" section of the
        Databases tab. Don't forget that PythonAnywhere databases start with your
        username + "$". For example, if your username is "user1234" and you named
        your database "loginexample" then your full database name will be
        "user1234$loginexample".

- Additional Configuration
    <br>You may set additional Flask configurations (e.g., DEBUG, MAX_CONTENT_LENGTH) in ims_app/__init__.py.

## Running the Application
To run the application locally:
```python
python run.py 
```
Access the app in your browser at ```http://localhost:5000```

## Deployment on PythonAnywhere
1. **Upload your Code**
    <br>Push your repository to GitHub and set it to private.
2. **Configure PythonAnywhere**
    * Create a new web app and choose Flask.
    * In the WSGI configuration file, point to your app. For example:
    ```python
    from run import app as application
    ```
    * Set environment variables as needed.
3. **Database Setup on PythonAnywhere**
    <br>Create the database (LCC_Issue_Tracker_db), then create the tables and populate using the provided SQL scripts and update ims_app/connect.py accordingly.

## Usage
* **Registration & Login**:
 <br>New users register via the signup page. New accounts are always assigned the "visitor" role by default.
* **Reporting Issues**:
 <br>Once logged in, users can report new issues, view their reported issues, and add comments.
* **Issue Management**:
 <br>Helpers and admins can view all unresolved issues, add comments that automatically update issue status, and view resolved issues on a separate page.
* **Profile Management**:
 <br>Users can update their profile details, change or remove their profile image, and update their password.
* **Admin Functions**:
 <br>Admins can view all users, search for users, and update user roles and statuses.
* **Test data populated**
 <br>The user account names and passwords (plaintext) are stored in password_hash_generator.py
 <br>For simplicity, their username and password are the same (even if it doesn't pass validation)
 <br>Visitor: `btaylor`, Helper: `tmitchell`, Admin: `rclarke`
 <br> A list of all other users: <br>
 ```
 sthompson, jwilson, mchen, doconnor, aparker, rpatel, efoster, mwilliams, lsmith, btaylor, alee, jbrown, kwood, dharris, sclark, pnguyen, ywood, gking, ewhite, rjones
 ```
 

## References & Credits
* Denied Access by Connor McManus: https://www.pexels.com/photo/red-and-white-signage-11795169/
* 404 photo by Markus Spiske: https://www.pexels.com/photo/don-t-panic-text-on-toilet-paper-3991795/
* User stickers created by <a href="https://www.flaticon.com/free-stickers/user" title="user stickers">Ina Mella - Flaticon</a>
* Fix icons created by <a href="https://www.flaticon.com/free-icons/fix" title="fix icons">Prosymbols Premium - Flaticon</a>

For additional details or troubleshooting, please look at the in-code documentation provided throughout the repository.
