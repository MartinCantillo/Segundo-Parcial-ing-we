
from flask import Flask, request, jsonify, json, render_template
from config import app, bd
from Model import Estudiante

@app.route("/loggin", methods=['POST'])
def estudiante():
    usuario = request.json['usuario'] 
    contraseña = request.json['contraseña']
    entrada = request.json['contraseña']
    salidad = request.json['salidad']
    newuser = Estudiante(usuario, contraseña)
    bd.session.add(newuser)
    bd.session.commit()     
    return "guardado"
