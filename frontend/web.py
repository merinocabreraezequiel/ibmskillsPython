#!/bin/env python
"""
Servidor Web en python para la solución de gestor de tareas
Uso::
    python web.py 8080
"""
import os
import sys
import json
import subprocess
import time

import http.server
import socketserver


#Si se lanza manualmente, recoge los argumentos para cambiar el puerto
if sys.argv[1:]:
  port = int(sys.argv[1])
else:
  port = 8080

def loadConfigs():
    """Carga el archivo de configuración y asigna las variables.

    Args: 
        None
    
    Return:
        Json
    
    Description:
        Carga el archivo ubicado en 'conf/config.json' y crea la variable con sus datos, en caso de error, registra el fallo y cierra la aplicación
    """
    try:
        f = open("../config/config.json", "r")
        string_double_quotes = f.read()
    except:
        sys.exit('ERROR CARGANDO ARCHVIO DE CONFIGURACIÓN EN FRONTEND')
    
    return(json.loads(string_double_quotes))


configure=loadConfigs()
"""Carga la configuración del archivo de configuracaión"""

class handlerhttp(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        """Carga el PATH de la aplicación para cargar la web"""
        path = super().translate_path(path)
        relpath = os.path.relpath(path, os.getcwd())
        return os.path.join(configure["webpath"], relpath)

with socketserver.TCPServer(('', port), handlerhttp) as httpd:
    print(f'Servidor web iniciado en http://localhost:{port}')
    httpd.serve_forever()