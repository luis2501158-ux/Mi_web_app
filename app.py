from flask import Flask

#vamos a crear un objeto de tipo flask

from flask_restful import Api, Resource

from resource import HelloWorld
from router import crear_rutas

app = Flask(__name__)


# Del objeto app ejecutamos el metodo run

api = Api(app)

crear_rutas(api)

app.run(port=8080, debug=True)
