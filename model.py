from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    nome = db.Column(db.String(80), nullable=False)
    data_nascimento = db.Column(db.Date, unique=False, nullable=False)
    data_inscricao = db.Column(db.Date, unique=False, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)


class Topico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    data_criacao = db.Column(db.Date, unique=False, nullable=False)
    data_ultimo_post = db.Column(db.Date, unique=False, nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String, nullable=False)
    data_post = db.Column(db.Date, unique=False, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey(Usuario.id), nullable=False)
    id_topico = db.Column(db.Integer, db.ForeignKey(Topico.id), nullable=False)



## TODO: Criar a classe Categoria e fazer a relação com topico
## Dica: Um topico pertence a UMA categoria (chave estrangeira)

