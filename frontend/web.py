#!/bin/env python
"""
ORisTIC like web for blustream python APIRest with Auth
Usage::
    python web.py 8080
Based on:
    https://blog.sverrirs.com/2016/11/simple-http-webserver-python.html
"""
import os
import sys
import json
import subprocess
import time


#skReading portnumber from command line
if sys.argv[1:]:
  port = int(sys.argv[1])
else:
  port = 8080

def loadConfigs():
    """Load config file and create needed objects.

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


def iniciar_servidores():
    """Enrutar una fuente en un destino.

    Args: 
        None
    
    Return:
        proceso_php <subprocess>: configuración de proceso para php
        proceso_nginx <subprocess>: configuración de proceso para nginx
    
    Description:
        crea las dos variables para servir la web en http y https
    """
    # Comando para iniciar PHP-FPM
    proceso_php = subprocess.Popen(["php-cgi.exe", "-b", "127.0.0.1:9000"])
    return proceso_php

def verificar_servidores(proceso_php, proceso_nginx):
    """Control de estado del servidor frontend.

    Args: 
        proceso_php <subprocess>: configuración de proceso para php
        proceso_nginx <subprocess>: configuración de proceso para nginx
    
    Return:
        None
    
    Description:
        Comprueba que el servidor esté opreativo cada 5 segundos y lo relanza en caso de error
    """
    while True:
        estado_php = proceso_php.poll()
        # Si algún proceso se detiene, lo reiniciamos
        if estado_php is not None:
            proceso_php = subprocess.Popen(["php-cgi.exe", "-b", "127.0.0.1:9000"])
        time.sleep(5)  # Espera 5 segundos antes de volver a verificar


configure=loadConfigs()
"""Carga la configuración del archivo de configuracaión"""

print("PHP Web Server started")
os.system('PHP -S '+configure["server"]+':'+str(port)+' -c php.ini -t .')
