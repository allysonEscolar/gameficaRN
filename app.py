from flask import Flask, render_template, flash, redirect, request, url_for, json
from data.database import db
from flask_migrate import Migrate
from flask_login import LoginManager
import os

from model.jogo import Jogo
from controller.JogoController import ControllerJogo

from model.usuario import Usuario
from controller.UsuarioController import bp_usuario

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Inicializa o LoginManager
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'usuario.login'  # Define a rota de login para redirecionar usuários não autenticados

@lm.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id)) 


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# string de conexao
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
database = os.getenv('DB_DATABASE')

conexao = app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}/{database}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Controladores
app.register_blueprint(ControllerJogo)
app.register_blueprint(bp_usuario)
