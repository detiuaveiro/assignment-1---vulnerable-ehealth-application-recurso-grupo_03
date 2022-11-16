from flask import Blueprint, render_template, flash,redirect, url_for, request
from flask_login import login_required, current_user
from .models import Appointment
from . import db
from datetime import datetime
apt = Blueprint("apt", __name__)


@apt.route("/appointment", methods=["GET"])
@login_required
def appointment():
    return render_template("appointment.html")

@apt.route("/appointment", methods=["POST"])
@login_required
def appointment_post():
    subject = request.form.get("subject")
    description = request.form.get("description")
    date = request.form.get("date")
    time = request.form.get("time")
    patientId = current_user.id

    new_appointment = Appointment(subject=subject, description=description, date=date, time=time, patientId=patientId)
    try:
        db.session.add(new_appointment)
        db.session.commit()
        flash("Your appointment has been scheduled. Thank you!")
        return redirect(url_for("main.index"))
    except Exception as e:
        print(e)
        flash("There was an issue scheduling your appointment. Please try again.")
        return redirect(url_for("main.index"))

@apt.route("/appointments", methods=["GET"])
@login_required
def appointments():
    if current_user.isAdmin:
        appointments = Appointment.query.all()
        return render_template("appointments.html", appointments=appointments)
    else:
        appointments = Appointment.query.filter_by(patientId=current_user.id).all()
        return render_template("appointments.html", appointments=appointments)