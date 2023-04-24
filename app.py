
from flask import Flask, request, jsonify, json, render_template
from config.bd import app, bd
from Model.Estudiante import estudiante, estudianteSchema
from Model.Categoria import Categoria, CategoriaSchema
from Model.Registro import registro, RegistroSchema

estudiante_schema = estudianteSchema()
estudiantes_schema = estudianteSchema(many=True)

profesor_schema = CategoriaSchema()
profesores_schema = CategoriaSchema(many=True)

Registro_schema = RegistroSchema()
Registros_schema = RegistroSchema(many=True)


@app.route("/estudiante", methods=['POST'])
def registrarEstudiante():
    codigoE = request.json['codigoE']
    nombre = request.json['nombre']
    contraseña = request.json['contraseña']
    newuser = estudiante(codigoE, nombre, contraseña)
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=9566)
