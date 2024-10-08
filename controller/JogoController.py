from flask import Blueprint, render_template, request, redirect, url_for, flash
from model.jogo import Jogo
from data.database import db
from flask_login import login_required

ControllerJogo = Blueprint('jogo', __name__, url_prefix='/')

# Lista de turmas
@ControllerJogo.route('/', methods=['GET'])
def recovery():
  jogos = Jogo.query.all()
  return render_template('index.html', dados=jogos)

# Cadastro
@ControllerJogo.route('/cadastro', methods=['GET'])
@login_required
def cadastroGET():
  return render_template('adicionarJogo.html')

@ControllerJogo.route('/cadastro', methods=['POST'])
@login_required
def cadastroPOST():
  nomeJogo = request.form.get("nomeJogo")
  disciplina = request.form.get("disciplina")
  conteudo = request.form.get("conteudo")
  descricao = request.form.get("descricao")
  link = request.form.get("link")
  
  jogo = Jogo(nomeJogo, disciplina, conteudo, descricao, link)
  db.session.add(jogo)
  db.session.commit()

  return redirect("/")


@ControllerJogo.route('/editar/<int:id>')
@login_required
def recovery_id(id):
  jogo = Jogo.query.get(id)
  return render_template('editarJogo.html', jogo=jogo)

@ControllerJogo.route('/editar/<int:id>', methods=["POST"])
@login_required
def update(id):
  jogo = Jogo.query.get(id)
  jogo.nomeJogo = request.form.get("nomeJogo")
  jogo.disciplina = request.form.get("disciplina")
  jogo.conteudo = request.form.get("conteudo")
  jogo.descricao = request.form.get("descricao")
  jogo.link = request.form.get("link")

  db.session.add(jogo)
  db.session.commit()
  flash('Jogo modificado com sucesso', 'success')
  
  return redirect("/")

@ControllerJogo.route('/apagar/<int:id>')
@login_required
def delete(id):
  jogo = Jogo.query.get(id)
  db.session.delete(jogo)
  db.session.commit()
  
  return redirect("/")


### Rotas removidas do app.py. É necessário criar um BluePrint especifica para elas

@ControllerJogo.route('/sobre')
def sobre():
    return render_template('sobre.html')

@ControllerJogo.route('/contato')
def contato():
    return render_template('contato.html')
