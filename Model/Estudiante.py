from config.bd import bd, app, ma

class estudiante(bd.Model):
    __tablename__ ='tblEstudiante'
    codigoE = bd.Column(bd.Integer, primary_key = True)
    nombre = bd.Column(bd.String(50))
    contraseña = bd.Column(bd.String(50))


    def __init__(self, codigoE,nombre,contraseña):
        self.codigoE = codigoE
        self.nombre =nombre
        self.contraseña = contraseña
    def __init__(self, codigoE):
        self.codigoE = codigoE
    


with app.app_context():
    bd.create_all()

class estudianteSchema(ma.Schema):
    class Meta:
        fields =( 'codigoE','nombre', 'contraseña')