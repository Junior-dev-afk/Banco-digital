from app import app
from flask import request, jsonify
from app.models.login.login import login
from app.models.register.register import register
from app.models.privateInfos.crud import crud
from app.models.pix.pix import pix


@app.route("/verifyLogin", methods = ["POST"])
def verifyLogin():

    data = request.get_json()

    user = data["user"]
    password = data["password"]

    return jsonify({"response" : login.login(user, password)})


@app.route("/setSession", methods = ["POST"])
def setSession ():

    data = request.get_json()

    user = data["user"]
    password = data["password"]

    return jsonify({"response" : login.verifyPassword(user, password)})


@app.route("/getRegister", methods = ["POST"])
def getRegister():

    data = request.get_json()

    user = data["user"]
    email = data["email"]
    cpf = data["cpf"]
    pass1 = data["pass1"]
    pass2 = data["pass2"]

    return jsonify({"response" : register.register(email, user, cpf, pass1, pass2)})


@app.route("/getUserInfos", methods = ["POST"])
def getUserInfos():
    
    data = request.get_json()

    user = data["user"]

    return jsonify({"response" : crud.read(user)})

@app.route("/enviarPix", methods = ["POST"])
def enviarPix ():
    
    data = request.get_json()

    pagador = data["pagador"]
    senha = data["senha"]
    chave = data["chave"]
    valor = data["valor"]

    return jsonify({"response" : pix.enviar(pagador, senha, chave, valor)})


@app.route("/verifyChavePix", methods = ["POST"])
def verifyChavePix ():

    data = request.get_json()

    chave = data["chave"]
    user = data["user"]

    return jsonify({"response" : crud.isChaveExistAndNotMy(chave, user)})


@app.route("/verifyValor", methods = ["POST"])
def verifyValor ():
    
    data = request.get_json()

    user = data["user"]
    valor = data["valor"]

    return jsonify({"response" : crud.haveMoneyInAccount(user, valor)})

@app.route("/getUserFromChave", methods = ["POST"])
def getUserFromChave ():
    
    data = request.get_json()

    chave = data["chave"]

    return jsonify({"response" : crud.getUserFromChavePix(chave)})