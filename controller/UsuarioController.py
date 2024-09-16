from flask import Blueprint, render_template, request, redirect, url_for, flash
from model.usuario import Usuario
from data.database import db, lm
from flask import Blueprint
from flask_login import login_user, logout_user

bp_usuario = Blueprint("usuario", __name__, template_folder='templates')


@bp_usuario.route('/login')
def login():
    return render_template('login.html')

@bp_usuario.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form['email'] 
    senha = request.form['senha']
    usuario = Usuario.query.filter_by(email = email).first()
    if(usuario and usuario.senha == senha):
        login_user(usuario)
        return redirect(url_for('jogo.recovery'))
    
        return 'logado'
        # return redirect('/')
    flash('Login ou senha incorretos')
    return redirect('login')    

@bp_usuario.route('/logoff')
def logoff():
	logout_user()
	return redirect(url_for('jogo.recovery'))