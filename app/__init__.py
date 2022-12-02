from flask import Flask, jsonify
from app.config import Config
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
cors = CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.app_context().push()

login = LoginManager(app)
login.login_view = 'login'


from app import models, topRoutes


@app.route('/', endpoint='hello')
def hello():
    return "Hello, World!"

@app.route('/profile',methods=['GET'], endpoint='profile')
def profile():
    return jsonify({'id':'1','name':'diego','email':'diego@utec.com','password':'1234'})

'''
from app.routes.login_bp import login_bp
from app.routes.user_bp import user_bp

app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(user_bp, url_prefix="/user")
'''
db.create_all()