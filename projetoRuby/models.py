#Criar a estrutura do banco de dados


from projetoRuby import database, login_maneger
from datetime import datetime
from flask_login import UserMixin

@login_maneger.user_loader
def load_usuario(id_user):
     return Usuario.query.get(int(id_user))



class Usuario(database.Model, UserMixin):
     id = database.Column(database.Integer, primary_key=True)
     name = database.Column(database.String, nullable=False)
     username = database.Column(database.String, nullable=False, unique=True)
     email = database.Column(database.String, nullable=False, unique=True)
     senha = database.Column(database.String, nullable=False)
     fotos = database.relationship("Foto", backref="usuario", lazy=True)
     descricao = database.Column(database.String, nullable=True)



class Foto(database.Model):
     id = database.Column(database.Integer, primary_key=True)
     imagem = database.Column(database.String, default = "default.png")
     data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
     id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)