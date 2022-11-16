from flask import Blueprint, render_template, flash,redirect, url_for, request
from flask_login import login_required, current_user
from flask import render_template,make_response
import pdfkit

tst = Blueprint("tst", __name__)

@tst.route("/test", methods=["GET"])
@login_required
def test():
    name = request.args.get('name', type=str)
    html = render_template(
        "certificate.html",
        name=name)
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response

@tst.route("/tests", methods=["GET"])
def tests():
    return render_template("tests.html")



