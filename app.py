
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
    newuser = estudiante( codigoE,nombre, contraseña)
    bd.session.add(newuser)
    bd.session.commit()
    return "guardado"


@app.route("/eliminar", methods=['POST'])
def eliminarEstudinte():
    id = request.json['codigoE']
    usuario = estudiante.query.get(id)
    bd.session.delete(usuario)
    bd.session.commit()
    return jsonify(estudiante_schema.dump(usuario))


@app.route("/actualizar", methods=['POST'])
def actualizaruser():
    id = request.json['codigoE']
    nombre = request.json['nombre']
    contraseña = request.json['contraseña']
    estudiante1 = estudiante.query.get(id)
    estudiante1.codigoE = id
    estudiante1.nombre = nombre
    estudiante1.contraseña = contraseña
    bd.session.commit()
    return "actualización exitosa"


@app.route("/categoria", methods=['POST'])
def SaveCategory():
    codigo = request.json['codigo']
    nombre = request.json['nombre']
    nombreCat = request.json['nombreCat']
    contraseña = request.json['contraseña']
    newuser = Categoria(codigo, nombre, nombreCat,  contraseña)
    bd.session.add(newuser)
    bd.session.commit()
    return "guardado"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9566)
