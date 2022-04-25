import os
from flask import Flask
from dotenv import load_dotenv
#importar el modulo para crear la api-rest
from flask_restful import Api
# modulo para conectar la Base de datos SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    #cargar las variables de entorno
    load_dotenv()

    # Configuraciones de la BD
    PATH = os.getenv("DATABASE_PATH")
    DB_NAME = os.getenv("DATABASE_NAME")

    # Comprobar en el SO  si existe la BD y si no existe la crea
    if not os.path.exists(f'{PATH}{DB_NAME}'):
        os.chdir(f'{PATH}')
        file = os.open(f'{DB_NAME}',os.O_CREAT)
    
    #INICIALIZAR LA APP DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{PATH}{DB_NAME}'
    
    db.init_app(app)

    # Creacion de las rutas
    import main.resources as resources
    api.add_resource(resources.ClientesResource,'/clientes')
    api.add_resource(resources.ClienteResource,'/cliente/<id>')
    api.add_resource(resources.UsuariosResource,'/usuarios')
    api.add_resource(resources.UsuarioResource,'/usuario/<id>')
    api.add_resource(resources.ProductosResource,'/productos')
    api.add_resource(resources.ProductoResource,'/producto/<id>')
    api.init_app(app)

    return app