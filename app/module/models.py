from app import db, flask_bcrypt, login
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
import json
import uuid
import string
import random
import datetime
	
# class Driver(db.Model):
# 	"""
# 	Driver model for storing driver related details
# 	"""
# 	__tablename__ = "drivers"

# 	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# 	full_name = db.Column(db.String(255), nullable=False)
# 	mobile_number = db.Column(db.String(15), nullable=False)
# 	profile_picture = db.Column(db.String(255), nullable=False)
# 	route_history = db.Column(db.String, nullable=True)

# 	def __repr__(self):
# 		return f"<Driver {self.id}>"

class pageInfo(db.Model):
	__tablename__ = "page_info"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	about = db.Column(db.String(), nullable=True)
	jhs = db.Column(db.String(), nullable=True)
	shs = db.Column(db.String(), nullable=True)
	uni = db.Column(db.String(), nullable=True)
	phone = db.Column(db.String(), nullable=True)
	email1 = db.Column(db.String(), nullable=True)
	email2 = db.Column(db.String(), nullable=True)
	theme = db.Column(db.Boolean, nullable=True)


class project(db.Model):
	__tablename__ = "project"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	img_url = db.Column(db.String(), nullable=True)
	name = db.Column(db.String(), nullable=True)
	about = db.Column(db.String(), nullable=True)
	typeof = db.Column(db.String(), nullable=True)
	date = db.Column(db.String(), nullable=True)
	category = db.Column(db.String(), nullable=True)

class jobExp(db.Model):
	__tablename__ = "job"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(), nullable=True)
	role = db.Column(db.String(), nullable=True)
	about = db.Column(db.String(), nullable=True)
	from_date = db.Column(db.String(), nullable=True)
	to_date = db.Column(db.String(), nullable=True)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
