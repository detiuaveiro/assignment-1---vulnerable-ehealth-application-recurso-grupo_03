from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from .models import User
from . import db

prof = Blueprint('profile', __name__)

#@prof.route('/change_password', methods=['POST'])
@prof.route('/change_password/<user>', methods=['POST'])
@login_required
#def change_password():
def change_password(user):
	# if user == 'admin':
		#password = request.form.get('password')
	newpassword = request.form.get('newpassword')
	confirmnewpassword = request.form.get('confirmnewpassword')
	user = User.query.filter_by(id=user.id).first()
	# user = User.query.filter_by(id="session["user"]?").first()
		# if user.password != password:
	if newpassword != confirmnewpassword:
		flash('Passwords do not match.')
		return redirect(url_for('/profile'))
	else:
		try:
			user.password = newpassword
			db.session.commit()
			flash('Password updated successfully.')
			return redirect(url_for('/profile'))
		except Exception as e:
			flash('There was an issue updating your password.')
			print(e)
			return redirect(url_for('/profile'))

# POR TESTAR, FALTA UM FORM, CWE ESTARÁ NA NÃO VERIFICAÇÃO DE SE O USER QUE PEDE PARA MUDAR A PASSWORD É O MESMO QUE ESTÁ LOGADO
# NÃO SEI ATÉ QUE PONTO ISTO NÃO É OUTRA CWE UMA VEZ QUE UTILIZA O URL PARA PASSAR O ID DO USER