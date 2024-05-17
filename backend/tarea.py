from datetime import datetime, timedelta

class Tarea:
    """
    Representa una tarea pendiente con estado (completada o pendiente).

    Atributos:
        descripcion (str): Descripción de la tarea.
        estado (bool): Indica si la tarea está completada (True) o pendiente (False).
    """

    estadosTarea = ['Pendiente', 'Completada', 'En Curso', 'Caducada', 'Descartada']

    def __init__(self, _titulo, _descripcion, _fechaCaducidad = (datetime.today() + timedelta(days = 1))):
        self.descripcion = _descripcion
        self.estado = self.estadosTarea[0]
        self.fecha = _fechaCaducidad
        self.titulo = _titulo
        print(self.titulo, self.descripcion, self.fecha, self.estado)

    def completar(self):
        """Marca la tarea como completada."""
        self.estado = self.estadosTarea[1]
    
    def actualizarFecha(self, _nuevaFecha):
        self.fecha = _nuevaFecha
    
    def pasarPendiente(self):
        self.estado = self.estadosTarea[0]
    
    def inciarTarea(self):
        self.estado = self.estadosTarea[2]
    
    def descartar(self):
        self.estado = self.estadosTarea[4]
    
    def caducidad(self):
        if self.fecha >= datetime.today():
            self.estado= self.estadosTarea[3]
            return self.estado
        else:
            return "Quedan "+str(self.fecha - datetime.today())+"días"

    def getInfo(self):
        """Devuelve los elementos que definen la tarea"""
        return self.titulo, self.descripcion, self.estado, self.fecha

