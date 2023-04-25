
from flask import Flask, request, jsonify, json, render_template
from config.bd import app, bd
from Model.Estudiante import estudiante, estudianteSchema
from Model.Categoria import Categoria, CategoriaSchema
from Model.Registro import registro, RegistroSchema
import datetime

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
def UpdateStudent():
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

@app.route("/registro", methods=['POST'])
def RegisterEntrada():
   # codigoR = request.json['codigoR']
   entrada =datetime.datetime.now()
   salida =datetime.datetime.now()
   #entrada = request.json['entrada']
   #salida = request.json['salida']
   estado = request.json['estado']
   idEstudiante = request.json['idEstudiante_fk']
   newuser = registro( entrada,salida, estado, idEstudiante)
   bd.session.add(newuser)
   bd.session.commit()
   return "guardado"

@app.route("/salida", methods=['POST'])
def RegisterSalida():
   # codigoR = request.json['codigoR']
   salida =datetime.datetime.now()
   idEstudiante = request.json['idEstudiante_fk']
   estado = request.json['estado']
   bd.session.query(registro).filter(
       registro.idEstudiante_fk==idEstudiante
   ).update(
        {
        registro.salida:salida,
        registro.estado : estado
         
        }
   )  
   bd.session.commit()
   return "guardado"

@app.route("/cat", methods=['POST'])
def consultarCategoria():
   # codigoR = request.json['codigoR']
   idCategoria_fk = request.json['idCategoria_fk']
   bd.session.query(registro).filter(
       
   ).update(
        {
        registro.idCategoria_fk:idCategoria_fk,
         
        }
   )  
   bd.session.commit()
   return "guardado"

@app.route('/trestablas',methods=['GET'])
def consultar():
    results = bd.session.query(estudiante, Categoria, registro). \
    select_from(estudiante).join(Categoria).join(registro).all()
    dato={}   
    i=0
    for users, taks, category in results:
        i+=1
        dato[i] = {
        'Nombre':users.fullname,
		'tarea':taks.nametak,
		'categoria':category.namecategory,                     
        }       
        print(users.fullname, taks.nametak, category.namecategory)
    return jsonify(dato)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9566)
