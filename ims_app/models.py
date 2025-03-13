"""
models.py

Provides helper functions for the LCC Issue Tracker to access data from the database,
such as retrieving the current user's profile information and session data.
"""

from flask import session
from ims_app import db

def get_session_data():
    """
    Retrieve the current session data.
    
    Returns:
        A dictionary representing the current session.
    """
    return session

def get_profile_data():
    """
    Retrieve the current user's profile data from the database.
    
    Returns:
        A dictionary containing the user's profile data, or None if the user is not logged in.
    """
    user_id = session.get('user_id')
    if not user_id:
        return None
    with db.get_cursor() as cursor:
        cursor.execute('''
                       SELECT *
                       FROM users 
                       WHERE user_id = %s;
                       ''', (user_id,))
        profile = cursor.fetchone()
    return profile