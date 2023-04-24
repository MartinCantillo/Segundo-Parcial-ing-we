from config.bd import bd, app, ma

class registro(bd.Model):
    __tablename__ ='tblregistro'
    codigoR = bd.Column(bd.Integer, primary_key = True)
    entrada = bd.Column(bd.String(50))
    salidad = bd.Column(bd.String(50))
    estado = bd.Column(bd.String(50))
    idEstudiante_fk = bd.Column(bd.Integer, bd.ForeignKey('tblEstudiante.codigoE'))
    idProfesor_fk = bd.Column(bd.Integer, bd.ForeignKey('tblcategoria.codigo'))

    def __init__(self, entrada,salidad,estado,idEstudiante_fk,idProfesor_fk):
        self.entrada = entrada
        self.salidad = salidad
        self.estado = estado
        self.idEstudiante_fk=idEstudiante_fk
        self.idProfesor_fk=idProfesor_fk

with app.app_context():
    bd.create_all()

class RegistroSchema(ma.Schema):
    class Meta:
        fields =( 'entrada', 'salidad','estado','idEstudiante_fk','idProfesor_fk')