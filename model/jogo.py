from data.database import db

class Jogo(db.Model):
  __tablename__="jogo"
  id         = db.Column(db.Integer, primary_key=True)
  nomeJogo   = db.Column(db.String(100))
  disciplina = db.Column(db.String(100))
  conteudo   = db.Column(db.String(300))
  descricao  = db.Column(db.String(500))

  def __init__(self, nomeJogo, disciplina, conteudo, descricao) :
    self.nomeJogo   = nomeJogo
    self.disciplina = disciplina
    self.conteudo   = conteudo
    self.descricao  = descricao

  def __repr__(self):
    return "Jogo: {}".format(self.nome)