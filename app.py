from flask import Flask, render_template, flash, redirect, request, url_for, json
from data.database import db
from flask_migrate import Migrate

from model.jogo import Jogo

from controller.JogoController import ControllerJogo

app = Flask(__name__)

app.config['SECRET_KEY'] = 'wdjdnjdnwdnwlqndlkdwmlkdeuhf4h4t48t5pt9r49-2--o23'

conexao = 'mysql+pymysql://desweb2024:D3sw3b1frn!@weblic2024.mysql.database.azure.com/web2024_gameficarn'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Controladores
app.register_blueprint(ControllerJogo)
