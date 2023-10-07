import json

from .arbolAVL import Arbol_AVL
from .proyectos import Proyecto

from arbolB.tareas import Tarea
from arbolB.arbolB import ArbolB
from listaEnlazada.listaEnlazada import ListaEnlazada

arbol = Arbol_AVL()
arbolB = ArbolB()
lista_enlazada = ListaEnlazada()

def cargar_json(file_path):
    with open(file_path,'r', encoding="utf-8") as archivo:
        datos = json.load(archivo)

    output = ""

    for proyecto in datos['Proyectos']:
        output += f"{proyecto['id']} | {proyecto['nombre']}\n"
        
        if len(proyecto['tareas']) == 0:
            output += "         |No hay Tareas\n"
        else:
            for tarea in proyecto['tareas']:
                str_tarea = f"{tarea['nombre']}" + " - " + f"{tarea['empleado']}"
                output += f"         | {str_tarea}\n"
                
        output += "\n"
        
    for i in range(len(datos['Proyectos'])):
        id_proyecto = datos['Proyectos'][i]['id']
        nombre_proyecto = datos['Proyectos'][i]['nombre']
        prioridad_proyecto = datos['Proyectos'][i]['prioridad']
        tareas_proyecto = datos['Proyectos'][i]['tareas']
        
        proyectos = Proyecto(id_proyecto, nombre_proyecto, prioridad_proyecto, tareas_proyecto)
        arbol.Insertar(proyectos)
        
        if len(tareas_proyecto) > 0:
            contador_tareas = 0
            for tarea in tareas_proyecto:
                contador_tareas += 1
                codigo_tarea = "T" + str(contador_tareas) + "-" + str(id_proyecto)
                tarea = Tarea(codigo_tarea, tarea['nombre'], tarea['empleado'], id_proyecto)
                arbolB.insertar(tarea)
                lista_enlazada.insertar(tarea)
            
    return output

def graficar_arbol():
    arbol.graficar()
    
def graficar_arbolB():
    arbolB.graficar()