from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, login
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from app.module.models import *
import json
import datetime

mod_auth = Blueprint('app', __name__)

@mod_auth.route('/')
def index():
	data = {
		"theme": ['None'] 
	}
	return render_template('index.html', **data)

@mod_auth.route('/admin_home')
def home():
	return render_template('dashboard.html')