from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, render_template, redirect, url_for, flash, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Usuario, Distritos, Intereses, Descripcion
from app.form import LoginForm
from app import db, app
import json

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='Home')

@app.route("/register", methods=['GET', 'POST'])
def register():
    body = request.get_json()
    try:     
        newUser = Usuario(nombre=body["nombre"], apellido=body["apellido"], email=body["email"], password=body["password"], edad=int(body["edad"]))
        db.session.add(newUser)
    except Exception as error:
        print("Invalid user", error)
        return "Invalid user"     
    finally:
        db.session.commit()  
        return "Usuario añadido"

@app.route('/get_user', methods=["POST", "GET"])
def getUser():
    body = request.get_json()
    user = Usuario.query.filter(Usuario.email == body["email"] and Usuario.password == body["password"]).first()
    desc = return_desc(user.id)
    if desc == None:
        desc = "No tiene descripcion"
    return json.dumps({"id": user.id, "nombre": user.nombre, "apellido": user.apellido, "edad": user.edad, "email": user.email, "password": user.password, "descripcion": desc})


@app.route('/users', methods=["POST", "GET"])
def getUsers():
    users = []
    user = Usuario.query.all()
    for usr in user:
        desc = return_desc(usr.id)
        if desc == None:
            desc = "No tiene descripcion"
        dist = return_distrito(usr.id)
        if dist == None:
            dist = "No hay distrito añadido"
        users.append({"id": usr.id, "nombre": usr.nombre, "apellido": usr.apellido, "edad": usr.edad, "email": usr.email, "password": usr.password, "descripcion":desc, "distrito":dist})
    return json.dumps(users)


@app.route('/users_dist/<distrito>', methods=["POST", "GET"])
def getUsersDist(distrito):
    users = []
    user = Usuario.query.all()
    for usr in user:
        desc = return_desc(usr.id)
        if desc == None:
            desc = "No tiene descripcion"
        dist = return_distrito(usr.id)
        if dist == None:
            dist = "No hay distrito añadido"
        if dist==distrito:
            users.append({"id": usr.id, "nombre": usr.nombre, "apellido": usr.apellido, "edad": usr.edad, "email": usr.email, "password": usr.password, "descripcion":desc, "distrito":dist})
    
    return json.dumps(users)


def return_desc(user_id):
    desc = []
    des = Descripcion.query.all()
    for d in des:
        desc.append({"user_id":d.user_id, "descripcion":d.descripcion})

    for i in range(len(desc)):
        if user_id == desc[i]["user_id"]:
            return desc[i]["descripcion"]



def return_distrito(user_id):
    desc = []
    des = Distritos.query.all()
    for d in des:
        desc.append({"user_id":d.user_id, "distrito":d.distrito})

    for i in range(len(desc)):
        if user_id == desc[i]["user_id"]:
            return desc[i]["distrito"]


@app.route('/descriptions', methods=["POST", "GET"])
def getDescriptions():
    users = []
    user = Descripcion.query.all()
    for usr in user:
        users.append({"user_id": usr.user_id, "descripcion": usr.descripcion})
    return json.dumps(users)

@app.route('/get_distritos', methods=["POST"])
def getDistrito():
    body = request.get_json()
    distritos = Distritos.query.filter(Distritos.user_id == body["id"]).all()
    desjson = json.dumps({"id": distritos.id, "distrito": distritos.distrito, "user_id":distritos.user_id})
    return desjson.description

@app.route('/get_descripcion', methods=["POST"])
def getDescripcion():
    body = request.get_json()
    descripcion = Descripcion.query.filter(Distritos.user_id == body["id"]).all()
    return json.dumps({"user_id":descripcion.user_id,"distrito": descripcion.descripcion})


@app.route("/add_distrito", methods=['GET', 'POST'])
def add_distrito():
    body = request.get_json()
    try:     
        newUser = Distritos(distrito=body["distrito"], user_id=body["user_id"])
        db.session.add(newUser)
    except Exception as error:
        print("Error añadiendo distrito", error)
        return "Error añadiendo distrito"     
    finally:
        db.session.commit()  
        return "Distrito añadido"

@app.route("/add_descripcion", methods=['GET', 'POST'])
def add_descripcion():
    body = request.get_json()
    try:     
        newUser = Descripcion(descripcion=body["descripcion"], user_id=body["user_id"])
        db.session.add(newUser)
    except Exception as error:
        print("Error añadiendo descripcion", error)
        return "Error añadiendo descripcion"     
    finally:
        db.session.commit()  
        return "Descripcion añadida"

@app.route("/add_intereses", methods=['GET', 'POST'])
def add_intereses():
    body = request.get_json()
    try:     
        newUser = Intereses(carrera=body["carrera"], user_id=body["user_id"])
        db.session.add(newUser)
    except Exception as error:
        print("Error añadiendo intereses", error)
        return "Error añadiendo intereses"     
    finally:
        db.session.commit()  
        return "Interes añadida"

@app.route('/search', methods=["POST", "GET"])
def search():
    body = request.get_json()
    users = []
    data = db.session.execute(f"select id, nombre, apellido, edad, email from usuario where id in ( select id from distritos where distrito = :distrito and id in ( select id from intereses where monto < :monto))", {"distrito": body["distrito"], "monto": body["monto"]})
    print(data)
    for row in data:
        users.append({"id": row[0], "nombre": row[1], "apellido": row[2], "edad": row[3]})
    return json.dumps(users)
