"""Handles the authentication view"""

from flask import  flash, make_response, redirect, render_template, request, session, url_for
from flask_jwt_extended import create_access_token, create_refresh_token
from web_app.views import web_views
from models import storage
from models.volunteer import Volunteer
from uuid import uuid4


@web_views.route('/create_account/submit', methods=['GET', 'POST'],
                 strict_slashes=False)
def create_account_submit():
    """Handles form submission for creating a new account"""
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')
    verify_password = request.form.get('verify_password')

    # Validate form data
    if not all([first_name, last_name, email, phone, password, verify_password]):
        flash('All fields are required.', 'error')
        return render_template('create-account.html',
                               cache_id=uuid4())

    if password != verify_password:
        flash('Passwords do not match.', 'error')
        return render_template('create-account.html',
                               cache_id=uuid4())

    # Check if email is already registered
    if storage.get_by_email(email):
        flash('Email is already registered. Please use a different email.', 'error')
        return render_template('create-account.html',
                               cache_id=uuid4())

    # Create new volunteer
    new_volunteer = Volunteer(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        password=password  # Password will be hashed in the model
    )
    storage.new(new_volunteer)
    storage.save()

    flash('Account created successfully! Please log in.', 'success')
    return redirect(url_for('web_views.login'))


@web_views.route('/login/submit', methods=['POST'], strict_slashes=False)
def login_submit():
    """Handles login form submission"""
    data = request.form  # Use request.form to get form data
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        flash('Missing email or password.', 'error')
        return render_template('login.html', cache_id=uuid4())
    
    # Get the user from the database
    user = storage.get_user_by_email(email)
    if not user or not user.check_password(password):
        flash('Bad email or password.', 'error')
        return render_template('login.html',
                               cache_id=uuid4())
    
    if not user or not user.check_password(password):
        flash('Incorrect email or password. Please try again.', 'error')
        return render_template('login.html', cache_id=uuid4()), 401

    # Create JWT tokens
    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    # Store tokens in cookies with expiration times
    response = make_response(redirect(url_for('web_views.display_dashboard')))
    response.set_cookie('access_token', access_token, httponly=True)
    response.set_cookie('refresh_token', refresh_token, httponly=True)

    session['user_id'] = user.id
    session['logged_in'] = True

    flash('Logged in successfully!', 'success')
    return response


@web_views.route('/logout', strict_slashes=False)
def logout():
    """Handles user logout"""
    # Clear the cookies
    response = make_response(redirect(url_for('web_views.login')))
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')

    session.pop('user_id', None)
    session.pop('logged_in', None)

    flash('Logged out successfully!', 'success')
    return response
