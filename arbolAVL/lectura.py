import json

from arbolAVL import Arbol_AVL

arbol = Arbol_AVL()

with open('datos.json','r') as archivo:
    datos = json.load(archivo)

for i in range(len(datos['Proyectos'])):
    print(datos['Proyectos'][i]['id'], '|', datos['Proyectos'][i]['nombre'])
    if len(datos['Proyectos'][i]['tareas']) > 0:
        for j in range(len(datos['Proyectos'][i]['tareas'])):
            print('\t','|',datos['Proyectos'][i]['tareas'][j]['nombre'], datos['Proyectos'][i]['tareas'][j]['empleado'])
    else:
        print('\t','|No hay Tareas')


for i in range(len(datos['Proyectos'])):
    arbol.Insertar(datos['Proyectos'][i]['id'])

arbol.graficar()