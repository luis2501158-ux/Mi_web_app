from resource import *

def crear_rutas(api):
    api.add_resource(pantalla_inicio, '/')
#quiero que puedas acceder a este recurso por medio de tal ruta
    api.add_resource(HelloWorld, '/hello')


