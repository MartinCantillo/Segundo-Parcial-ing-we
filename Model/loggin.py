from config.bd import bd, app, ma

class loggin(bd.Model):
    __tablename__ ='loggin'
    id = bd.Column(bd.Integer, primary_key = True)
    usuario = bd.Column(bd.String(50))
    contraseña = bd.Column(bd.String(50))



    def __init__(self, usuario,contraseña):
        self.namusuarioetak = usuario
        self.contraseña = contraseña

with app.app_context():
    bd.create_all()

class estudianteSchema(ma.Schema):
    class Meta:
        fields =('usuario', 'contraseña')