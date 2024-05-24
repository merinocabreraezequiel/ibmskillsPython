from threading import Thread
#from waitress import serve
import json
from time import localtime, sleep, strftime, localtime, time
import pdoc
from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
import os
import sys

from tarea import Tarea

app = Flask(__name__)
"""Inicia Flask. """
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
"""Activa CORS en la app. """
api = Api(app, prefix="/v1")
"""Definición de la estructura de la API """
auth = HTTPBasicAuth()
"""Archivo de autenticación Básica """

USER_DATA = {
    "gestor": "ContrasenaSuperSecreta"
}
"""json de User/Password para la API"""

def loadConfigs():
    """Carga el archivo de configuración.

    Args: 
        None
    
    Return:
        Json
    
    Description:
        Carga el archivo ubicado en 'conf/config.json' y crea la variable con sus datos, en caso de error, registra el fallo y cierra la aplicación
    """
    try:
        f = open("config/config.json", "r")
        string_double_quotes = f.read()
    except:
        sys.exit('ERROR CARGANDO ARCHVIO DE CONFIGURACIÓN')
    
    return(json.loads(string_double_quotes))

def runFrontEndSrv():
    """Inicializador de frontend.

    Args: 
        None
    
    Return:
        None
    
    Description:
        Crea un thread con la aplicación de frontend, lo inicia y realiza una pausa antes de continuar
    """
    frontEndthread = Thread(target=FrontEndSrv) # Define the Thread with the function
    frontEndthread.start() # Start the Thread
    sleep(5)

def FrontEndSrv():
    """Lanzador de frontend.

    Args: 
        None
    
    Return:
        None
    
    Description:
        Lanza el Servidor Web
    """
    os.system('cd '+str(configure["path"])+'\\frontend && python .\\web.py')

@auth.verify_password
def verify(username, password):
    """Check the user/password validation.

    Args: 
        username <string>: username to validate
        password <string>: password to validate
    
    Return:
        noname <bool>: check if correpond
    
    Description:
        Return [true/false] checking with references
    """
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class nuevaTarea(Resource):
    """Enrutar una fuente en un destino.

    Args: 
        destino <string>: código del decoder
        origen <string>: código del encoder
    
    Return:
        returnJson <json>: output de la respuesta de ACM500 con la información de la asignación
    
    Description:
        Asigna desde el ACM500 a un decoder un encoder, recoge la repuesta y devuelve la estructura los datos en un json
    """
    @auth.login_required
    def get(self, titulo, descripcion, fecha):
        global tareas

        returnData = {}
        try:
            nueva_tarea = Tarea(titulo, descripcion, fecha)
            print(len(tareas))
            tareas[len(tareas)] = nueva_tarea
            print(len(tareas))
            returnData['success'] = True
            returnData['message'] = None
        except:
            returnData['success'] = False
            returnData['message'] = None

        returnJSON = json.dumps(returnData)
        return returnJSON 

class listarTareas(Resource):
    """Enrutar una fuente en un destino.

    Args: 
        destino <string>: código del decoder
        origen <string>: código del encoder
    
    Return:
        returnJson <json>: output de la respuesta de ACM500 con la información de la asignación
    
    Description:
        Asigna desde el ACM500 a un decoder un encoder, recoge la repuesta y devuelve la estructura los datos en un json
    """
    @auth.login_required
    def get(self):
        returnData = {}
        try:
            returnData['success'] = True
            if len(tareas)>0:
                returnData['tareas']={}
                for i in tareas:
                    returnData['tareas'][i]={}
                    _tit, _desc, _est, _fetch = tareas[i].getInfo()
                    returnData['tareas'][i]['id'] = i
                    returnData['tareas'][i]['titulo'] = _tit
                    returnData['tareas'][i]['descripcion'] = _desc
                    returnData['tareas'][i]['estado'] = _est
                    returnData['tareas'][i]['fecha'] = _fetch
            returnData['message'] = None
        except:
            returnData['success'] = False
            returnData['message'] = None

        returnJSON = json.dumps(returnData)
        return returnJSON 

class retrasarTarea(Resource):
    """Enrutar una fuente en un destino.

    Args: 
        destino <string>: código del decoder
        origen <string>: código del encoder
    
    Return:
        returnJson <json>: output de la respuesta de ACM500 con la información de la asignación
    
    Description:
        Asigna desde el ACM500 a un decoder un encoder, recoge la repuesta y devuelve la estructura los datos en un json
    """
    @auth.login_required
    def get(self, id):
        returnData = {}
        try:
            nueva_tarea = Tarea(titulo, descripcion, fecha)
            tareas[len(tareas)] = nueva_tarea
            returnData['success'] = True
            returnData['message'] = None
        except:
            returnData['success'] = False
            returnData['message'] = None

        returnJSON = json.dumps(returnData)
        return returnJSON 

class completarTarea(Resource):
    """Enrutar una fuente en un destino.

    Args: 
        destino <string>: código del decoder
        origen <string>: código del encoder
    
    Return:
        returnJson <json>: output de la respuesta de ACM500 con la información de la asignación
    
    Description:
        Asigna desde el ACM500 a un decoder un encoder, recoge la repuesta y devuelve la estructura los datos en un json
    """
    @auth.login_required
    def get(self, id):
        returnData = {}
        try:
            nueva_tarea = Tarea(titulo, descripcion, fecha)
            tareas[len(tareas)] = nueva_tarea
            returnData['success'] = True
            returnData['message'] = None
        except:
            returnData['success'] = False
            returnData['message'] = None

        returnJSON = json.dumps(returnData)
        return returnJSON 

class volverPendiente(Resource):
    """Enrutar una fuente en un destino.

    Args: 
        destino <string>: código del decoder
        origen <string>: código del encoder
    
    Return:
        returnJson <json>: output de la respuesta de ACM500 con la información de la asignación
    
    Description:
        Asigna desde el ACM500 a un decoder un encoder, recoge la repuesta y devuelve la estructura los datos en un json
    """
    @auth.login_required
    def get(self, id):
        returnData = {}
        try:
            nueva_tarea = Tarea(titulo, descripcion, fecha)
            tareas[len(tareas)] = nueva_tarea
            returnData['success'] = True
            returnData['message'] = None
        except:
            returnData['success'] = False
            returnData['message'] = None

        returnJSON = json.dumps(returnData)
        return returnJSON 

class descartarTarea(Resource):
    """Enrutar una fuente en un destino.

    Args: 
        destino <string>: código del decoder
        origen <string>: código del encoder
    
    Return:
        returnJson <json>: output de la respuesta de ACM500 con la información de la asignación
    
    Description:
        Asigna desde el ACM500 a un decoder un encoder, recoge la repuesta y devuelve la estructura los datos en un json
    """
    @auth.login_required
    def get(self, id):
        returnData = {}
        try:
            nueva_tarea = Tarea(titulo, descripcion, fecha)
            tareas[len(tareas)] = nueva_tarea
            returnData['success'] = True
            returnData['message'] = None
        except:
            returnData['success'] = False
            returnData['message'] = None

        returnJSON = json.dumps(returnData)
        return returnJSON 

@app.errorhandler(404)
def page_not_found(error):
   return {"succes": False, "error":404, "message":"404 Not Found"}, 404

@app.errorhandler(401)
def unathorized_user(error):
   return {"succes": False, "error":401, "message":"401 Not Authorized"}, 401

@app.errorhandler(500)
def internal_server_error(error):
   return {"succes": False, "error":500, "message":"500 Server Error"}, 500

 
api.add_resource(nuevaTarea, '/nt/<string:titulo>/<string:descripcion>/<string:fecha>')
api.add_resource(listarTareas, '/lt')
api.add_resource(retrasarTarea, '/rt/<int:id>')
api.add_resource(completarTarea, '/ct/<int:id>')
api.add_resource(volverPendiente, '/vp/<int:id>')
api.add_resource(descartarTarea, '/dt/<int:id>')

configure=""
"""<json> con la configuración del sistema."""

tareas = {}
"""<colleccion> tareas"""

if __name__ == '__main__':
    configure=loadConfigs()
    runFrontEndSrv()
    app.run(debug=False,host="0.0.0.0")