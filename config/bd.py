from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/parcial2/MartinCantillo2020'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False