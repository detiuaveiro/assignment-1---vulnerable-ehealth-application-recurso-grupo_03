from flask import Blueprint, render_template
from flask_login import login_required
from mysql.connector import connect
main = Blueprint('app', __name__, template_folder='templates', static_folder='static')

connection = connect(
    host="localhost",
    port=5051,
    user="root",
    password="password",
    database="ehealth"
)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('index.html')
