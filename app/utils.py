from flask import Blueprint, url_for, jsonify
from app import db
from app.models import User, Appointment

utl = Blueprint('util', __name__)


@utl.route('/util/generate/users', methods=['GET'])
def generateusers():
    db.session.execute("DELETE FROM user WHERE isAdmin = false;")
    db.session.commit()
    users =[{
        "name": "Glory Powley",
        "email": "gpowley0@noaa.gov",
        "password": "a8dQZpjEg",
        "isAdmin": False
    }, {
        "name": "Kele Jonsson",
        "email": "kjonsson1@redcross.org",
        "password": "78liTxLTt",
        "isAdmin": False
    }, {
        "name": "Minnaminnie Darlison",
        "email": "mdarlison2@oaic.gov.au",
        "password": "L7H7yH",
        "isAdmin": False
    }, {
        "name": "Novelia Ford",
        "email": "nford3@usda.gov",
        "password": "ddCodJiCIE2",
        "isAdmin": False
    }, {
        "name": "Bradney Andrioli",
        "email": "bandrioli4@gravatar.com",
        "password": "Jv0SvfT",
        "isAdmin": False
    }, {
        "name": "Katherine Geater",
        "email": "kgeater5@csmonitor.com",
        "password": "gLesmOzwA",
        "isAdmin": False
    }, {
        "name": "Kerianne Diggar",
        "email": "kdiggar6@sun.com",
        "password": "OMS1yy0CuBZh",
        "isAdmin": False
    }, {
        "name": "Katharine Callacher",
        "email": "kcallacher7@baidu.com",
        "password": "j48nxuG9",
        "isAdmin": False
    }, {
        "name": "Maribelle McGilroy",
        "email": "mmcgilroy8@msu.edu",
        "password": "saqZZwOi6ja",
        "isAdmin": False
    }, {
        "name": "Ignacius MacCaffery",
        "email": "imaccaffery9@rambler.ru",
        "password": "6lmhKnR9",
        "isAdmin": False
    }]
    try:
        db.session.bulk_insert_mappings(User, users)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})


@utl.route('/util/generate/admin', methods=['GET'])
def generateadmin():
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
        "patientId": 1,
        "subject": "1319",
        "date": "8/2/2022",
        "time": "1:23 AM",
        "description": "Puncture wound without foreign body of unspecified shoulder, sequela"
    }, {
        "patientId": 8,
        "subject": "544",
        "date": "9/24/2022",
        "time": "5:34 PM",
        "description": "Pedestrian injured in unspecified traffic accident, sequela"
    }, {
        "patientId": 9,
        "subject": "8446",
        "date": "10/5/2022",
        "time": "12:05 PM",
        "description": "Non-follicular (diffuse) lymphoma, unspecified, lymph nodes of head, face, and neck"
    }, {
        "patientId": 8,
        "subject": "8865",
        "date": "1/25/2022",
        "time": "9:50 AM",
        "description": "Displaced fracture of proximal phalanx of unspecified thumb, subsequent encounter for fracture with delayed healing"
    }, {
        "patientId": 2,
        "subject": "8332",
        "date": "8/3/2022",
        "time": "10:47 PM",
        "description": "Intentional self-harm by drowning and submersion after jump into swimming pool"
    }, {
        "patientId": 2,
        "subject": "0784",
        "date": "2/27/2022",
        "time": "8:29 AM",
        "description": "Subluxation of other carpometacarpal joint of right hand, initial encounter"
    }, {
        "patientId": 7,
        "subject": "6093",
        "date": "3/20/2022",
        "time": "8:16 AM",
        "description": "Unspecified fracture of unspecified ilium, initial encounter for closed fracture"
    }, {
        "patientId": 6,
        "subject": "8127",
        "date": "12/19/2021",
        "time": "9:37 AM",
        "description": "Other congenital malformations of pancreas and pancreatic duct"
    }, {
        "patientId": 9,
        "subject": "8372",
        "date": "7/11/2022",
        "time": "3:23 AM",
        "description": "Unspecified intracapsular fracture of left femur, subsequent encounter for open fracture type IIIA, IIIB, or IIIC with nonunion"
    }, {
        "patientId": 10,
        "subject": "5492",
        "date": "10/13/2022",
        "time": "1:44 PM",
        "description": "Superficial frostbite of neck, initial encounter"
    }]
    try:
        db.session.bulk_insert_mappings(Appointment, appointments)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})
