import pdfkit
from flask import Blueprint, request, render_template, make_response
from flask_login import login_required

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


