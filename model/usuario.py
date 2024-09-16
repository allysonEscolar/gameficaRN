from data.database import db

from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
  __tablename__= "usuario"
  id = db.Column(db.Integer, primary_key = True)
  nome = db.Column(db.String(100))
  email = db.Column(db.String(100))
  senha = db.Column(db.String(100))

  def __init__(self, nome, email, senha):
    self.nome = nome
    self.email = email
    self.senha = senha

  def get_id(self):
      return str(self.id)