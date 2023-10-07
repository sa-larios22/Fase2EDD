from .nodoEnlazado import Nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, tarea):
        nuevo = Nodo(tarea)
        if not self.cabeza:
            self.cabeza = nuevo
            return
        ultimo = self.cabeza
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo

    def imprimir(self):
        if not self.cabeza:
            print("Lista vacia")
            return
        
        actual = self.cabeza
        while actual:
            print(actual.tarea.codigo + " - " + actual.tarea.nombre + " - " + actual.tarea.empleado + " - " + str(actual.tarea.proyecto))
            actual = actual.siguiente

    def buscar_por_empleado(self, empleado):
        actual = self.cabeza
        coincidencias = []
        
        while actual:
            print(actual.tarea.empleado)
            if actual.tarea.empleado == empleado:
                coincidencias.append(actual.tarea)
            actual = actual.siguiente
            
        return coincidencias