from flask import Blueprint, jsonify
from app import db
from app.models import User, Appointment, Report

utl = Blueprint('util', __name__)


@utl.route('/util/generate/users', methods=['GET'])
def generate_users():
    db.session.execute("DELETE FROM user WHERE isAdmin = false;")
    db.session.commit()
    users = [{
        "name": "Glory Powley",
        "email": "gpowley0@noaa.gov",
        "password": "a8dQZpjEg",
        "isAdmin": False,
        "image": "a.png"
    }, {
        "name": "Kele Jonsson",
        "email": "kjonsson1@redcross.org",
        "password": "78liTxLTt",
        "isAdmin": False,
        "image": "b.png"
    }, {
        "name": "Minnaminnie Darlison",
        "email": "mdarlison2@oaic.gov.au",
        "password": "L7H7yH",
        "isAdmin": False,
        "image": "c.png"
    }, {
        "name": "Novelia Ford",
        "email": "nford3@usda.gov",
        "password": "ddCodJiCIE2",
        "isAdmin": False,
        "image": "d.png"
    }, {
        "name": "Bradney Andrioli",
        "email": "bandrioli4@gravatar.com",
        "password": "Jv0SvfT",
        "isAdmin": False,
        "image": "e.png"
    }, {
        "name": "Katherine Geater",
        "email": "kgeater5@csmonitor.com",
        "password": "gLesmOzwA",
        "isAdmin": False,
        "image": "f.png"
    }, {
        "name": "Kerianne Diggar",
        "email": "kdiggar6@sun.com",
        "password": "OMS1yy0CuBZh",
        "isAdmin": False,
        "image": "g.png"
    }, {
        "name": "Katharine Callacher",
        "email": "kcallacher7@baidu.com",
        "password": "j48nxuG9",
        "isAdmin": False,
        "image": "h.png"
    }, {
        "name": "Maribelle McGilroy",
        "email": "mmcgilroy8@msu.edu",
        "password": "saqZZwOi6ja",
        "isAdmin": False,
        "image": "i.png"
    }, {
        "name": "Ignacius MacCaffery",
        "email": "imaccaffery9@rambler.ru",
        "password": "6lmhKnR9",
        "isAdmin": False,
        "image": "j.png"
    }]
    try:
        db.session.bulk_insert_mappings(User, users)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})


@utl.route('/util/generate/admin', methods=['GET'])
def generate_admin():
    db.session.execute("DELETE FROM user WHERE isAdmin = true;")
    db.session.commit()

    admin = User(name="Admin", email="admin@admin.com", password="admin", isAdmin=True)
    try:
        db.session.add(admin)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})


@utl.route('/util/generate/appointments', methods=['GET'])
def generate_appointments():
    users = User.query.all()
    if len(users) < 10:
        return jsonify({'success': False, 'message': 'Not enough users to generate appointments'})

    db.session.execute("DELETE FROM appointment;")
    appointments = [{
        "patientId": 3,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "9/9/2022",
        "description": "Spontaneous abortion, complicated by delayed or excessive hemorrhage, unspecified",
        "code": "8536425261"
    }, {
        "patientId": 7,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "2/17/2022",
        "description": "Old bucket handle tear of medial meniscus",
        "code": "6280159361"
    }, {
        "patientId": 1,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "9/11/2022",
        "description": "Open wound(s) (multiple) of unspecified site(s), without mention of complication",
        "code": "4127982381"
    }, {
        "patientId": 4,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "6/6/2022",
        "description": "Obstruction by abnormal pelvic soft tissues during labor, delivered, with or without mention of antepartum condition",
        "code": "0877142262"
    }, {
        "patientId": 8,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "10/27/2022",
        "description": "Other motor vehicle nontraffic accident while boarding and alighting injuring passenger in motor vehicle other than motorcycle",
        "code": "4171699363"
    }, {
        "patientId": 2,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "11/19/2021",
        "description": "Acute nonparalytic poliomyelitis, poliovirus type I",
        "code": "0148986021"
    }, {
        "patientId": 4,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "4/1/2022",
        "description": "Unspecified surgical operations and procedures causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation",
        "code": "5709499218"
    }, {
        "patientId": 3,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "6/22/2022",
        "description": "Acute myocardial infarction of anterolateral wall, subsequent episode of care",
        "code": "6960288371"
    }, {
        "patientId": 10,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "5/26/2022",
        "description": "Open fracture of subtrochanteric section of neck of femur",
        "code": "1223488934"
    }, {
        "patientId": 2,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "5/23/2022",
        "description": "Subacute myeloid leukemia, without mention of having achieved remission",
        "code": "7553929948"
    }]
    try:
        db.session.bulk_insert_mappings(Appointment, appointments)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})

@utl.route('/util/generate/reports', methods=['GET'])
def generate_reports():
    db.session.execute("DELETE FROM report;")
    reports = [{
        "patientId": 3,
        "date": "9/9/2022",
        "description": "Spontaneous abortion, complicated by delayed or excessive hemorrhage, unspecified",
        "code": "8536425261"
    }, {
        "patientId": 7,
        "date": "2/17/2022",
        "description": "Old bucket handle tear of medial meniscus",
        "code": "6280159361"
    }, {
        "patientId": 1,
        "date": "9/11/2022",
        "description": "Open wound(s) (multiple) of unspecified site(s), without mention of complication",
        "code": "4127982381"
    }, {
        "patientId": 4,
        "date": "6/6/2022",
        "description": "Obstruction by abnormal pelvic soft tissues during labor, delivered, with or without mention of antepartum condition",
        "code": "0877142262"
    }, {
        "patientId": 8,
        "date": "10/27/2022",
        "description": "Other motor vehicle nontraffic accident while boarding and alighting injuring passenger in motor vehicle other than motorcycle",
        "code": "4171699363"
    }, {
        "patientId": 2,
        "date": "11/19/2021",
        "description": "Acute nonparalytic poliomyelitis, poliovirus type I",
        "code": "0148986021"
    }, {
        "patientId": 4,
        "date": "4/1/2022",
        "description": "Unspecified surgical operations and procedures causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation",
        "code": "5709499218"
    }, {
        "patientId": 3,
        "date": "6/22/2022",
        "description": "Acute myocardial infarction of anterolateral wall, subsequent episode of care",
        "code": "6960288371"
    }, {
        "patientId": 10,
        "date": "5/26/2022",
        "description": "Open fracture of subtrochanteric section of neck of femur",
        "code": "1223488934"
    }, {
        "patientId": 2,
        "date": "5/23/2022",
        "description": "Subacute myeloid leukemia, without mention of having achieved remission",
        "code": "7553929948"
    }]

    try:
        db.session.bulk_insert_mappings(Report, reports)
        db.session.commit()

        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})
