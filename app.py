from flask import Flask, render_template, flash, redirect, request, url_for, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    arquivo = open("static/jogos.json")
    dados = json.load(arquivo)
    return render_template('index.html', dados=dados)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form["email"]
    senha = request.form["senha"]
    if (email=="admin@email.com" and senha=="123"):
        return render_template('telaAdmin.html')
    else:
        flash('E-mail ou senha inválidos', 'danger')
        flash('Tente novamente', 'warning')

        return redirect(url_for('login'))


@app.route('/adicionarJogo')
def adicionarJogo():
    return render_template('adicionarJogo.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')
