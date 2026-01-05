from flask_restful import Resource

from flask import make_response, render_template

class pantalla_inicio(Resource):
    def get(self):
        contenido = render_template('index.html')
        return make_response(contenido)

#Vamos a crear recursos
class HelloWorld(Resource):
    def get(self):

        return "Esta es la pantalla inicio"

