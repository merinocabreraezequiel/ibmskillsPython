from threading import Thread
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
    frontEndthread = Thread(target=FrontEndSrv)
    frontEndthread.start()
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
    """Vala usuario y contraseña para la API.

    Args: 
        username <string>: username a validar
        password <string>: password a validar
    
    Return:
        noname <bool>: check if correpond
    
    Description:
        Return [true/false] checking with references
    """
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class nuevaTarea(Resource):
    """Crea nueva tarea y la agrega a la array.

    Args: 
        titulo <string>: titulo de la tarea
        descripcion <string>: descripcion de la tarea
        fecha <string>: fecha de finalización de la tarea
    
    Return:
        returnJson <json>: Información de si la carga se ha producido correctamente
    
    Description:
        Crea un nuevo elemento de la clase Tarea y la añade a al Array de tareas, devuelve un json con la información de si ha sido satisfactoria o no
    """
    @auth.login_required
    def get(self, titulo, descripcion, fecha):
        global tareas

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

class listarTareas(Resource):
    """Crea un listado de tareas registradas.

    Args: 
        None
    
    Return:
        returnJson <json>: Listado de tareas con todos sus datos
    
    Description:
        Revisa el array de tareas y carga la información de todas las tareas que encuentra, las formatea y las agrega a un json
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

class actualizarTitulo(Resource):
    """Actualiza el titulo de una tarea.

    Args: 
        id <string>: id de la tarea a actualizar
        titulo <string>: nuevo titulo de la tarea
    
    Return:
        returnJson <json>: json con información de correción o fallo
    
    Description:
        Realiza la modificación del titulo del elemento id de la lsita de tareas
    """
    @auth.login_required
    def get(self, id, titulo):
        returnData = {}
        try:
            tareas[id].updateTitulo(titulo)
            returnData['success'] = True
            returnData['message'] = None
        except:
            returnData['success'] = False
            returnData['message'] = None

        returnJSON = json.dumps(returnData)
        return returnJSON


class actualizarDescripcion(Resource):
    """Actualiza la descripción de una tarea.

    Args: 
        id <string>: id de la tarea a actualizar
        descripcion <string>: nueva descripción de la tarea
    
    Return:
        returnJson <json>: json con información de correción o fallo
    
    Description:
        Realiza la actualización de la descripción de la tarea
    """
    @auth.login_required
    def get(self, id, desc):
        returnData = {}
        try:
            tareas[id].updateDescripcion(desc)
            returnData['success'] = True
            returnData['message'] = None
        except:
            returnData['success'] = False
            returnData['message'] = None

        returnJSON = json.dumps(returnData)
        return returnJSON

class actualizarFecha(Resource):
    """Enrutar una fuente en un destino.

    Args: 
        id <string>: id de la tarea a actualizar
        fecha<string>: nueva fecha de la tarea
    
    Return:
        returnJson <json>: json con información de correción o fallo
    
    Description:
        Realiza la modificación de la fecha del elemento id de la lsita de tareas
    """
    @auth.login_required
    def get(self, id, fecha):
        returnData = {}
        try:
            tareas[id].updateFecha(fecha)
            returnData['success'] = True
            returnData['message'] = None
        except:
            returnData['success'] = False
            returnData['message'] = None

        returnJSON = json.dumps(returnData)
        return returnJSON

class cambiarEstado(Resource):
    """Enrutar una fuente en un destino.

        Args: 
        id <string>: id de la tarea a actualizar
        estado <string>: nuevo estado de la tarea
    
    Return:
        returnJson <json>: json con información de correción o fallo
    
    Description:
        Realiza la modificación del estado del elemento id de la lsita de tareas
    """
    @auth.login_required
    def get(self, id, estado):
        returnData = {}
        try:
            tareas[id].updateEstado(int(estado))
            returnData['success'] = True
            returnData['message'] = None
        except:
            returnData['success'] = False
            returnData['message'] = None

        returnJSON = json.dumps(returnData)
        return returnJSON

class eliminarTarea(Resource):
    """Enrutar una fuente en un destino.

    Args: 
        id <string>: id de la tarea a eliminar
    
    Return:
        returnJson <json>: json con información de correción o fallo
    
    Description:
        Elimina el elemento id de la lista de tareas
    """
    @auth.login_required
    def get(self, id):
        returnData = {}
        try:
            tareas.pop(id)
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


api.add_resource(listarTareas, '/lt') 
api.add_resource(nuevaTarea, '/nt/<string:titulo>/<string:descripcion>/<string:fecha>')
api.add_resource(eliminarTarea, '/et/<int:id>')
api.add_resource(cambiarEstado, '/ce/<int:id>/<int:estado>')
api.add_resource(actualizarTitulo, '/at/<int:id>/<string:titulo>')
api.add_resource(actualizarDescripcion, '/ad/<int:id>/<string:desc>')
api.add_resource(actualizarFecha, '/af/<int:id>/<string:fecha>')

configure=""
"""<json> con la configuración del sistema."""

tareas = {}
"""<colleccion> tareas"""

if __name__ == '__main__':
    configure=loadConfigs()
    runFrontEndSrv()
    app.run(debug=False,host="0.0.0.0")