
from flask import Flask, request, jsonify, json, render_template
from config import app, bd
from Model import Estudiante , loggin

@app.route("/estudiante", methods=['POST'])
def registrar():
    usuario = request.json['usuario'] 
    contraseña = request.json['contraseña']
    newuser = Estudiante(usuario, contraseña)
    bd.session.add(newuser)
    bd.session.commit()     
    return "guardado"


@app.route("/loggin", methods=['POST'])
def loggin():
    usuario = request.json['usuario'] 
    contraseña = request.json['contraseña']
    newuser = loggin(usuario, contraseña)
    bd.session.add(newuser)
    bd.session.commit()     
    return "guardado"

