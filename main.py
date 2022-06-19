#
#pip install requests, flask, flask_restful
#

#DATABASE USER

#END OF DATABASE USER

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Producto_info(Resource):
    def get(self):
        return None

class Usuario_info(Resource):
    def get(self, name, test):
        return {"data": name, "test": test}
    
    def post(self):
        return {"data": "Posted"}
    
#api.add_resource(Usuario_info, "/usuario_info")
api.add_resource(Usuario_info, "/usuario_info/<string:name>/<int:test>")

if __name__ == '__main__':
    app.run(debug=True)
