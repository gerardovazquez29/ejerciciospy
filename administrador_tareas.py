
import textwrap

class Tarea:
    def __init__(self,descripcion, categoria, detalles):
        self._descripcion = descripcion
        self._categoria = categoria
        self._detalles = detalles
        self._estado = "pendiente"

    @property
    def descripcion(self):
        return self._descripcion
    @property
    def categoria(self):
        return self._categoria

    @property
    def detalles(self):
        return self._detalles

    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, nuevo_estado):
        self._estado = nuevo_estado
    def mostrar(self):
        ancho = 80

        str_detalles = f'Detalles: {self._detalles}'
        if len(str_detalles) > ancho:
            detalles = textwrap.fill(str_detalles, width=ancho)
        else:
            detalles = str_detalles
        print('='*ancho)
        print(f'Tarea: {self._descripcion}')
        print('='*ancho)
        print(f'Categoría: {self._categoria}')
        print('='*ancho)
        print(f'Estado: {self._estado}')
        print('='*ancho)
        print(detalles)
        print('='*ancho)

Tarea1 = Tarea("Preparar informe", "Trabajo", "Escribir informe de 20 paginas")
Tarea1.mostrar()

tarea2 = Tarea("llamar cientes", "Trabajo", "Realizar llamada a los 23 clientes y verificar que los productos han llegado correctamente y no hay novedades")
tarea2.mostrar()

tarea2.estado = "completada"
tarea2.mostrar()

class Administrador:
    def __init__(self):
        self._tareas = []

    @property
    def tareas(self):
        return self._tareas
    
    def mostrar(self, categoria=None):
        if len(self._tareas) != 0:
            ancho_col = 80
            
           
        
