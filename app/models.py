from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctorId = db.Column(db.Integer, db.ForeignKey('user.id'))
    patientId = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date())
    description = db.Column(db.String(1000))

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    specialization = db.Column(db.String(100))
    description = db.Column(db.Integer)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    salary = db.Column(db.Integer)

class Drug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100))
    company = db.Column(db.String(100))

class Specialization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000))
