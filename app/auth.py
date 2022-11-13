from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
import sqlite3

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))
    else:
        return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    db = sqlite3.connect('instance/db.sqlite')
    result = db.execute("SELECT * FROM user WHERE email = '"+email+"' AND password = '"+password+"';").fetchall()

    if not result:
        flash('Please check your login details and try again.')
        db.close()
        return redirect(url_for('auth.login'))

    db.close()

    user = User.query.filter_by(email=email).first()
    login_user(user)
    return redirect(url_for('main.profile'))


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

