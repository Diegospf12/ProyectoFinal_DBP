from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

'''
class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.Date())
'''

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(64), nullable=False, index=True)
    apellido = db.Column(db.String(64), nullable=False, index=True)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    edad = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Intereses(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    carrera = db.Column(db.String(64), nullable=False)
    monto = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

class Descripcion(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    descripcion = db.Column(db.String(64), nullable=False)
    # fotos = db.Column(db.String(64), db.ForeignKey('user.username'), nullable=False)

class Distritos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    distrito = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    user_id_1 = db.Column(db.Integer, db.ForeignKey('usuario.id'))

class Dislikes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    user_id_1 = db.Column(db.Integer, db.ForeignKey('usuario.id'))

# class Matches(db.Model):
@login.user_loader
def load_user(id):
    return Usuario.query.get(int(id))