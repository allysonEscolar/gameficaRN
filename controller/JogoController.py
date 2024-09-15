from flask import Blueprint, render_template, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from model.jogo import Jogo
from data.database import db

ControllerJogo = Blueprint('jogo', __name__, url_prefix='/')

# Lista de turmas
@ControllerJogo.route('/', methods=['GET'])
def recovery():
  jogos = Jogo.query.all()
  return render_template('index.html', dados=jogos)

# Cadastro
@ControllerJogo.route('/cadastro', methods=['GET'])
def cadastroGET():
  return render_template('adicionarJogo.html')

@ControllerJogo.route('/cadastro', methods=['POST'])
def cadastroPOST():
  nomeJogo = request.form.get("nomeJogo")
  disciplina = request.form.get("disciplina")
  conteudo = request.form.get("conteudo")
  descricao = request.form.get("descricao")

  jogo = Jogo(nomeJogo, disciplina, conteudo, descricao)
  db.session.add(jogo)
  db.session.commit()

  return redirect("/")


@ControllerJogo.route('/editar/<int:id>')
def recovery_id(id):
  jogo = Jogo.query.get(id)
  return render_template('editarJogo.html', jogo=jogo)

@ControllerJogo.route('/editar/<int:id>', methods=["POST"])
def update(id):
  jogo = Jogo.query.get(id)
  jogo.nomeJogo = request.form.get("nomeJogo")
  jogo.disciplina = request.form.get("disciplina")
  jogo.conteudo = request.form.get("conteudo")
  jogo.descricao = request.form.get("descricao")

  db.session.add(jogo)
  db.session.commit()
  
  return redirect("/")

@ControllerJogo.route('/apagar/<int:id>')
def delete(id):
  jogo = Jogo.query.get(id)
  db.session.delete(jogo)
  db.session.commit()
  
  return redirect("/")

### Rotas removidas do app.py. É necessário criar um BluePrint especifica para elas

@ControllerJogo.route('/login')
def login():
    return render_template('login.html')

@ControllerJogo.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form["email"]
    senha = request.form["senha"]
    if (email=="admin@email.com" and senha=="123"):
        return render_template('telaAdmin.html')
    else:
        flash('E-mail ou senha inválidos', 'danger')
        flash('Tente novamente', 'warning')

        return redirect(url_for('login'))

@ControllerJogo.route('/sobre')
def sobre():
    return render_template('sobre.html')

@ControllerJogo.route('/contato')
def contato():
    return render_template('contato.html')
