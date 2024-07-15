#!/usr/bin/python3
"""Entry point for User Profile page"""

from web_app.views import web_views
from flask import render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import storage
from models.volunteer import Volunteer


@web_views.route('/user_profile', methods=['GET'], strict_slashes=False)
@jwt_required()
def display_dashboard():
    """Handles user profile page"""
    current_user_id = get_jwt_identity()
    user = storage.get_user_by_id(current_user_id)
    return render_template('volunteer-dashboard.html',
                           user=user)
    