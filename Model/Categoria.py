from config.bd import bd, app, ma

class Categoria(bd.Model):
    __tablename__ ='tblcategoria'
    codigo = bd.Column(bd.Integer, primary_key = True)
    nombre = bd.Column(bd.String(50))
    nombreCat = bd.Column(bd.String(50))
    contraseña = bd.Column(bd.String(50))

    def __init__(self,codigo, nombre,nombreCat,contraseña):
        self.codigo=codigo
        self.nombre = nombre
        self.nombreCat = nombreCat
        self.contraseña=contraseña

with app.app_context():
    bd.create_all()

class CategoriaSchema(ma.Schema):
    class Meta:
        fields =( 'codigo', 'nombre','nombreCat','contraseña')