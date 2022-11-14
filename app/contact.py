from flask import Blueprint, request, flash, redirect, url_for, render_template
from .models import Contact
from . import db

ctc = Blueprint('ctc', __name__)


@ctc.route('/contact')
def contact():
	print("hello")
	return render_template('contact.html')


@ctc.route('/contact', methods=['POST'])
def contact_post():
	name = request.form.get('name')
	email = request.form.get('email')
	phone = request.form.get('phone')
	message = request.form.get('message')

	new_contact = Contact(name=name, email=email, phone=phone, message=message)
	try:
		db.session.add(new_contact)
		db.session.commit()
		flash('Your message has been sent. Thank you!')
		return redirect(url_for('main.index'))
	except:
		flash('There was an issue sending your message. Please try again.')
		return redirect(url_for('main.index'))