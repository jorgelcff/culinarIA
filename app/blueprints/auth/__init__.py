from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

from app.blueprints.auth import auth