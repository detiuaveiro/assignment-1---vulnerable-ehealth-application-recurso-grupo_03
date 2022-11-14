from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from app import db
from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/createpatient', methods=['GET'])
def createpatient():
    new_patient = User(name="Bob", email="bob@bob.com", password="123", isAdmin=False)
    try:
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('main.index'))
    except:
        return redirect(url_for('main.index'))