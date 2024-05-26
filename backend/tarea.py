from datetime import datetime, timedelta

class Tarea:
    """Elemento de tipo tarea.

    Args: 
        none
    
    Return:
        none
    
    Description:
        Define un objeto tarea que se define en su init y se puede actalizar cada uno de sus elementos independientemente
    """

    """Listado de opciones de estado, se gestionan con numeros, no con los textos"""
    estadosTarea = ['Pendiente', 'Completada', 'En Curso', 'Caducada', 'Descartada']

    def __init__(self, _titulo, _descripcion, _fechaCaducidad = (datetime.today() + timedelta(days = 1))):
        """Inicia el elemento tarea con todas sus opciones.

        Args: 
            _titulo <string>: titulo de la tarea
            _descripcion <string>: descripción de la tarea
            _fechaCaducidad <string>: fecha limite de la tarea
        
        Return:
            None
        
        Description:
            Recive los parametros de creación, el de fecha si es nulo se establece a día de mañana, el estado se define como Pendiente por defecto
        """
        self.descripcion = _descripcion
        self.estado = self.estadosTarea[0]
        self.fecha = _fechaCaducidad
        self.titulo = _titulo
    
    def updateFecha(self, _nuevaFecha):
        """Actualiza la fecha con la recivida por parametros"""
        self.fecha = _nuevaFecha
    
    def updateTitulo(self, _titulo):
        """Actualiza el titulo con el recivido por parametros"""
        self.titulo = _titulo

    def updateDescripcion(self, _descripcion):
        """Actualiza la descripción con la recivida por parametros"""
        self.descripcion = _descripcion

    def updateEstado(self, _codigoEstado):
        """Actualiza el estado mediante el código recibido por parametros"""
        self.estado = self.estadosTarea[_codigoEstado]
    
    def caducidad(self):
        """FUNCIÓN NO UTILIZADA de revisión de estado, pensada para futuras iteraciones"""
        if self.fecha >= datetime.today():
            self.estado= self.estadosTarea[3]
            return self.estado
        else:
            return "Quedan "+str(self.fecha - datetime.today())+"días"

    def getInfo(self):
        """Devuelve los elementos que definen la tarea"""
        return self.titulo, self.descripcion, self.estado, self.fecha

