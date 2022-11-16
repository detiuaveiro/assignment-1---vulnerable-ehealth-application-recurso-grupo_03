from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask
from flask_login import login_required, current_user
from .models import User
from . import db
import os

prof = Blueprint('profile', __name__)

@prof.route('/profile')
@login_required
def profile():
	user = User.query.filter_by(id=current_user.id).first()
	return render_template('profile.html', user=user)

@prof.route('/edit_profile/')
@login_required
def edit_page(id):
	user = User.query.filter_by(id=current_user.id).first()
	return render_template('edit_profile.html', user=user)

@prof.route('/edit_profile', methods=['POST'])
@login_required
def edit_profile():
	email = request.form.get('email')
	address = request.form.get('address')
	contact = request.form.get('contact')
	image = request.files.get('image')
	if image and not image.filename.endswith('.png') and not image.filename.endswith('.jpeg'):
		flash('Please upload a png or jpeg image.')
		return redirect(url_for('profile.edit_profile'))
	
	password = request.form.get('password')
	user = User.query.filter_by(id=current_user.id).first()
	
	if password and current_user.password == password:
		new_password = request.form.get('new_password')
		if new_password:
			confirm_new_password = request.form.get('confirm_new_password')
			if new_password == confirm_new_password:
				user.password = new_password
			else:
				flash('Passwords do not match.')
				return redirect(url_for('profile.edit_profile'))

		if email:
			user.email = email
		if address:
			user.morada = address
		if contact:
			user.contact = contact
		if image:
			user.image = image.filename
			image.save(os.path.join("app/static/pictures",image.filename))
		db.session.commit()
	else:
		flash('Wrong password.')
		return redirect(url_for('profile.edit_profile'))
	
	flash('Updated successfully.')
	return redirect(url_for('profile.profile'))