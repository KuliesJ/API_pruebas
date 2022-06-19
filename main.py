#
#pip install requests, flask, flask_restful
#

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Usuario_info(Resource):
    def get(self):
        return {
                "Nombre": "Don Pepito",
                "Correo": "DonPepito@DonJose.com",
                "Password": "incorrecta",
                "Carrito": {
                        "Producto1": "Cubo_ejemplo",
                        "Producto2": "Cubo_ejemplo2"
                        }
                }
    
api.add_resource(Usuario_info, "/usuario_info")

if __name__ == '__main__':
    app.run(debug=True)