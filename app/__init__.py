from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config import config_by_name
from flask import Flask, render_template, redirect
from flask_login import LoginManager, current_user, login_user

# Define the WSGI application object
app = Flask(__name__)
db = SQLAlchemy(app)
flask_bcrypt = Bcrypt()
db.init_app(app)
flask_bcrypt.init_app(app)
login = LoginManager(app)

# Configurations
app.config.from_object(config_by_name['dev'])

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return "<center><h1>Sorry, resource not found.</h1></center>"

@app.errorhandler(500)
def not_found(error):
	return "<center><h1>Sorry, there has been a server error, please contact sys admin</h1></center>"

@app.login_manager.unauthorized_handler
def unauth_handler():
	return redirect('/')

# Import a module / component using its blueprint handler variable (mod_auth)
from app.module.controllers import mod_auth as auth_module

# Register blueprint(s)
app.register_blueprint(auth_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()