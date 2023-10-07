from arbolB.tareas import Tarea

class Nodo:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None