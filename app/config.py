import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #coger nuestras variables de entorno (en .flaskenv) el URL de conexion para la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'postgresql://postgres:1234@localhost:5432/postgres'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
