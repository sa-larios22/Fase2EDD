import json

from .arbolAVL import Arbol_AVL

arbol = Arbol_AVL()

def cargar_json(file_path):
    with open(file_path,'r') as archivo:
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
        arbol.Insertar(datos['Proyectos'][i]['id'])
    
    return output

def graficar_arbol():
    arbol.graficar()