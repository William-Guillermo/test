from .. import db
import datetime as dt

class Usuario(db.Model):
    #cracion de a tabla dentro del modelo Usuario
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True, index=True)
    role = db.Column(db.String(45),nullable=False, default="cliente")
    telefono=db.Column(db.Integer, nullable=False)
    fecha_registro = db.Column(db.DateTime, default=dt.datetime.now(),nullable=False)

     #metodo solo para debuguear y representar el objeto usuario
    def __repr__(self):
        return (f'{self.nombre}')
    
    # a la hora de devolver el recurso se tiene que enviar como objeto json
    def to_json(self):
        usuario_json = {
        'id': self.id,
        'nombre': self.nombre,
        'apellido': self.apellido,
        'email': self.email,
        'telefono': self.telefono,
        'role': self.role,
        'fecha': str(self.fecha_registro)  # la fecha puede llegar a ser un objeto por eso la conversion
        } 
        #cuando llamemos al metodo que retorne ese json
        return  usuario_json

    #metodo Enviar para agregar  un recurso json desde front, metodo estatico sin instanciar la clase
    @staticmethod 
    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        email = usuario_json.get('email')
        telefono = usuario_json.get('telefono')
        role = usuario_json.get('role')
        fecha_registro = usuario_json.get('fecha_registro')
        return Usuario(        #una vez recibido el json lo resturnamos como objeto Python y lo instanciamos
            id = id,
            nombre = nombre,
            apellido = apellido,
            email = email,
            telefono = telefono,
            role = role,
            fecha_registro = fecha_registro,

        )


    
    

