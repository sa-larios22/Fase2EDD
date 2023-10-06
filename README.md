# EDD_2S2023_PY_202111849
Primer Proyecto - Estructuras de Datos - Segundo Semestre 2023

## Manual Técnico
El presente proyecto utiliza distintas estructuras de datos para la organización de proyectos de una compañía de marketing digital, el fin del mismo es dar organización a los empleados, proyectos y tareas de la empresa.
Se utilizó el lenguaje __C++__ y se implementaron las estructuras:
- Lista Doblemente Enlazada
- Lista Doblemente Enlazada Circular
- Cola de Prioridad
- Matriz

### Clase Main
Clase principal de la aplicación en la que se unen los métodos para el manejo de datos y las estructuras.

<details>
  <summary> Código </summary>
  <br>

``` c++
#include <iostream>
#include <cstdlib>
#include <string>

#include "ListaDEC.h"
#include "ListaDE.h"
#include "ColaPrioridad.h"
#include "Matriz.h"

using namespace std;

string defaultUsername = "1";
string defaultPassword = "1";

string usernameInput = "";
string passwordInput = "";

void menuAdministrador();
void pressEnterToContinue();
void cargarEmpleados();
void cargaManual();
void cargaMasiva();
void verEmpleados();
void crearProyecto();
void asignarProyecto();
void crearTareas();
void asignarTareas();

ListaDEC *listaDEC = new ListaDEC();
ListaDE *listaDE = new ListaDE();
ColaPrioridad *cola = new ColaPrioridad();
Matriz *matrizN = new Matriz();

int numero_empleado_backend = 0;
int numero_empleado_frontend = 0;
int numero_empleado_qa = 0;

void login(){
    cout << "" << endl;
    cout << "**********          EDD ProjectUp          **********" << endl;
    cout << "Usuario: ";
    cin >> usernameInput;
    cout << "Password: ";
    cin >> passwordInput;

    if (usernameInput == defaultUsername && passwordInput == defaultPassword) {
        menuAdministrador();
    } else {
        cout << "Credenciales incorrectas" << endl;
        login();
    }
}

void pressEnterToContinue() {
    std::string entrada;

    cout << "" << endl;
    cout << "Presione enter para regresar" << endl;
    cout << "" << endl;

    cin.ignore();
    std::getline(std::cin, entrada);
}

void menuAdministrador(){
    cout << "" << endl;
    cout << "**********          EDD ProjectUp          **********" << endl;
    cout << "**********   Bienvenido " << usernameInput << "         **********" << endl;
    cout << " 1. Cargar empleados " << endl;
    cout << " 2. Crear Proyecto " << endl;
    cout << " 3. Asignar Proyecto " << endl;
    cout << " 4. Crear Tareas " << endl;
    cout << " 5. Asignar Tareas " << endl;
    cout << " 6. Regresar " << endl;
    cout << " 7. Salir " << endl;
    cout << "" << endl;


    string entrada = "";
    cout << "Ingrese el numero de la opción que desea: ";
    cin >> entrada;

    if (entrada == "1") {
        cargarEmpleados();
    } else if (entrada == "2") {
        crearProyecto();
    } else if (entrada == "3") {
        asignarProyecto();
    } else if (entrada == "4") {
        crearTareas();
    } else if (entrada == "5") {
        asignarTareas();
    } else if (entrada == "6") {
        login();
    } else if (entrada == "7") {
        exit(0);
    } else {
        cout << "" << endl;
        cout << "Ingrese una opción válida" << endl;
        menuAdministrador();
    }
}

void cargarEmpleados() {
    cout << "" << endl;
    cout << "**********          EDD ProjectUp          **********" << endl;
    cout << "**********   Bienvenido " << usernameInput << "         **********" << endl;
    cout << "**********     Menú Carga de Empleados     **********" << endl;
    cout << " 1. Carga manual" << endl;
    cout << " 2. Carga masiva" << endl;
    cout << " 3. Ver Listado de Empleados" << endl;
    cout << " 4. Regresar" << endl;

    string entrada = "";
    cout << "Ingrese el numero de la opción que desea: ";
    cin >> entrada;

    if (entrada == "1") {
        cargaManual();
    } else if (entrada == "2") {
        cargaMasiva();
    } else if (entrada == "3") {
        verEmpleados();
    } else if (entrada == "4") {
        menuAdministrador();
    } else {
        cout << "Ingrese una opción válida" << endl;
        cargarEmpleados();
    }
}

void cargaManual() {

    std::string nombre_empleado;
    std::string contrasena_empleado;

    cout << "Ingrese el nombre del empleado: ";
    cin.ignore();
    std::getline(std::cin, nombre_empleado);

    cout << "Ingrese la contraseña del empleado: ";
    std::cin >> contrasena_empleado;

    try {

        listaDEC->InsertarDEC(nombre_empleado, contrasena_empleado);
        cout << "" << endl;
        cout << "Empleado registrado" << endl;

    } catch (exception) {

        cout << "Error al registrar el empleado" << endl;

    }

    cargarEmpleados();

}

void cargaMasiva() {

    string nombre_archivo;

    cout << "" << endl;
    cout << "Ingrese el nombre del archivo CSV (incluya su extension)" << endl;

    cin >> nombre_archivo;

    try {

        listaDEC -> leerArchivo(nombre_archivo);
        cout << "Carga masiva exitosa" << endl;

    } catch (exception) {

        cout << "Error al realizar la carga masiva" << endl;

    }

    cargarEmpleados();
}

void verEmpleados() {

    listaDEC->verListaDEC();

    pressEnterToContinue();

    cargarEmpleados();

}

void crearProyecto() {
    cout << "" << endl;
    cout << "**********          EDD ProjectUp          **********" << endl;
    cout << "**********   Bienvenido " << usernameInput << "         **********" << endl;
    cout << "**********      Menú Carga de Proyecto     **********" << endl;

    string nombre_nuevo_proyecto = "";
    string prioridad_nuevo_proyecto = "";

    cout << "Nombre del Proyecto: ";
    cin.ignore();
    std::getline(std::cin, nombre_nuevo_proyecto);

    cout << "Tipo de Prioridad: ";
    cin >> prioridad_nuevo_proyecto;

    cola->Encolar(nombre_nuevo_proyecto, prioridad_nuevo_proyecto);

    cout << "" << endl;

    cola->Ordenar();

    cola->VerProyectos();

    cout << "" << endl;

    cola->Graficar();

    pressEnterToContinue();

    menuAdministrador();
}

void asignarProyecto() {
    cout << "" << endl;
    cout << "**********          EDD ProjectUp          **********" << endl;
    cout << "**********   Bienvenido " << usernameInput << "         **********" << endl;
    cout << "**********     Asignacion de Proyectos     **********" << endl;

    std::string nombre_empleado;
    std::string posicion_empleado;
    std::string codigo_proyecto;

    cin.ignore();

    listaDEC->verListaDEC();

    cout << "Nombre del empleado: " ;
    std::getline(cin, nombre_empleado);

    cout << "**********   PUESTOS DE TRABAJO   **********" << endl;
    cout << " 1. Frontend " << endl;
    cout << " 2. Backend " << endl;
    cout << " 3. Quality Assurance " << endl;

    cout << "Ingrese el numero de opcion de la posicion del empleado: ";
    std::getline(cin, posicion_empleado);

    string codigo_empleado;

    if (posicion_empleado == "1") {
        numero_empleado_backend += 1;
        codigo_empleado = (numero_empleado_backend < 100 ? (numero_empleado_backend < 10 ? "BDEV-00"+std::to_string(numero_empleado_backend) : "BDEV-0"+std::to_string(numero_empleado_backend)): "BDEV-"+std::to_string(numero_empleado_backend));

        NodoListaDEC *aux = listaDEC->Primero;
        bool encontrado = false;

        do {

            if (aux->EmpleadoSistema->Nombre == nombre_empleado) {

                aux->EmpleadoSistema->Codigo = codigo_empleado;
                encontrado = true;
                break;
            }
            aux = aux->Siguiente;

        } while (aux != listaDEC->Primero);

    } else if (posicion_empleado == "2") {

        numero_empleado_frontend += 1;
        codigo_empleado = (numero_empleado_frontend  < 100 ? (numero_empleado_frontend  < 10 ? "FDEV-00"+std::to_string(numero_empleado_frontend) : "FDEV-0"+std::to_string(numero_empleado_frontend)): "FDEV-"+std::to_string(numero_empleado_frontend));

        NodoListaDEC *aux = listaDEC->Primero;
        bool encontrado = false;

        do {

            if (aux->EmpleadoSistema->Nombre == nombre_empleado) {

                aux->EmpleadoSistema->Codigo = codigo_empleado;
                encontrado = true;
                break;
            }
            aux = aux->Siguiente;

        } while (aux != listaDEC->Primero);

    } else if (posicion_empleado == "3") {

        numero_empleado_qa += 1;
        codigo_empleado = (numero_empleado_qa  < 100 ? (numero_empleado_qa  < 10 ? "QA-00"+std::to_string(numero_empleado_qa) : "QA-0"+std::to_string(numero_empleado_qa)): "QA-"+std::to_string(numero_empleado_qa));

        NodoListaDEC *aux = listaDEC->Primero;
        bool encontrado = false;

        do {

            if (aux->EmpleadoSistema->Nombre == nombre_empleado) {

                aux->EmpleadoSistema->Codigo = codigo_empleado;
                encontrado = true;
                break;
            }
            aux = aux->Siguiente;

        } while (aux != listaDEC->Primero);

    } else {

        cout << "" << endl;
        cout << "Ingrese una opción válida" << endl;
        cout << "" << endl;

        pressEnterToContinue();

        menuAdministrador();
    }


    cola->VerProyectos();

    cout << "Codigo del proyecto: ";
    std::getline(cin, codigo_proyecto);

    try {

        while (cola->Primero) {
            matrizN->insertar_proyecto(cola);
            cola->Descolar();
        }

        matrizN->insertar_empleado(listaDEC);

        matrizN->asignarProyecto(nombre_empleado, codigo_proyecto);

        matrizN->Graficar();

        cout << "Proyecto asignado correctamente" << endl;

    } catch (exception) {
        cout << "Error al asignar el proyecto" << endl;
    }

    pressEnterToContinue();

    menuAdministrador();
}

void crearTareas() {
    cout << "" << endl;
    cout << "**********          EDD ProjectUp          **********" << endl;
    cout << "**********   Bienvenido " << usernameInput << "         **********" << endl;
    cout << "**********           Crear Tarea           **********" << endl;

    string codigo_nueva_tarea;
    string nombre_tarea;

    cout << "Codigo del proyecto al que va la tarea: ";
    cin.ignore();
    std::getline(std::cin, codigo_nueva_tarea);

    cout << "Descripcion de la tarea: ";
    //cin.ignore();
    std::getline(std::cin, nombre_tarea);

    try {

        listaDE->InsertarDE(codigo_nueva_tarea, nombre_tarea, "Sin encargado");

    } catch (exception) {

        cout << "Error al insertar la tarea" << endl;

    }

    listaDE->verListaDE();

    pressEnterToContinue();

    menuAdministrador();

}

void asignarTareas() {
    cout << "" << endl;
    cout << "**********          EDD ProjectUp          **********" << endl;
    cout << "**********   Bienvenido " << usernameInput << "         **********" << endl;
    cout << "**********      Asignacion de Tareas       **********" << endl;

    string codigo_proyecto;
    string nombre_tarea;
    string encargado;

    cola->VerProyectos();

    cout << "Código del proyecto de la tarea: ";
    cin.ignore();
    std::getline(std::cin, codigo_proyecto);

    listaDE->verListaDE();

    cout << "Nombre de la tarea: ";
    cin.ignore();
    std::getline(std::cin, nombre_tarea);

    listaDEC->verListaDEC();

    cout << "Nombre del encargado: ";
    cin.ignore();
    std::getline(std::cin, encargado);

    listaDE->verListaDE();

    pressEnterToContinue();

    menuAdministrador();



}



int main()
{
    login();
    return 0;
}

```
  
</details>

### Clase Empleado
La clase "Empleado" representa la información de un empleado en un sistema. Tiene un constructor que toma el nombre y la contraseña del empleado para inicializar los atributos correspondientes. El constructor también inicializa otros atributos, como el código y el puesto del empleado. La clase no realiza acciones específicas en su destructor. En conjunto, esta clase encapsula la información básica de un empleado en un sistema.

<details>
  <summary> Código </summary>
  <br>

```Empleado::Empleado(std::string nombre, std::string password):``` Este es el constructor de la clase Empleado, que toma dos parámetros: nombre y contraseña.

```this->Codigo = "";:``` Inicializa el miembro Codigo de la instancia de Empleado con una cadena vacía.  
```this->Nombre = nombre;:``` Asigna el valor del parámetro nombre al miembro Nombre.  
```this->Password = password;:``` Asigna el valor del parámetro password al miembro Password.  
```this->Puesto = "";:``` Inicializa el miembro Puesto de la instancia de Empleado con una cadena vacía.  

``` c++
#include "Empleado.h"
#include <string>

Empleado::Empleado(std::string nombre, std::string password)
{
    this->Codigo = "";
    this->Nombre = nombre;
    this->Password = password;
    this->Puesto = "";
}

```
</details>

### Clase Nodo Lista Doblemente Enlazada Circular
La clase NodoListaDEC se utiliza en una estructura de datos de lista doblemente enlazada circular. Cada nodo almacena un puntero a un objeto Empleado y dos punteros, uno al nodo siguiente y otro al nodo anterior en la lista.

<details>
  <summary> Código </summary>
  <br>

``` C++
#include "NodoListaDEC.h"

NodoListaDEC::NodoListaDEC(std::string nombre, std::string password)
{
    this->Siguiente = 0;
    this->Anterior = 0;
    this->EmpleadoSistema = new Empleado(nombre, password);
}
```
  
</details>

### Clase Lista Doblemente Enlazada Circular
La clase ListaDEC representa una lista doblemente enlazada circular que almacena información de empleados los empleados en las anteriores clases en forma de nodos.

Constructor ```ListaDEC()```: Inicializa la lista estableciendo el puntero Primero en nulo y el tamaño en 0.

Método ```InsertarDEC(std::string nombre, std::string password)```: Inserta un nuevo nodo en la lista con la información del empleado proporcionada. Si la lista está vacía, crea el primer nodo. Si no está vacía, encuentra el último nodo, enlaza el nuevo nodo con él y cierra el círculo enlazando el primer nodo con el nuevo.

Método ```verListaDEC()```: Muestra por consola los nombres y contraseñas de los empleados almacenados en la lista.

Método ```leerArchivo(std::string nombre_archivo)```: Lee un archivo CSV, ignora la primera línea (encabezado) y luego procesa las líneas restantes, extrayendo nombres y contraseñas para crear nodos de empleado y agregarlos a la lista.

<details>
  <summary> Código </summary>
  <br>

``` C++
#include "ListaDEC.h"
#include <string>
#include <limits>


ListaDEC::ListaDEC()
{
    this->Primero = 0;
    this->Tamanio = 0;
}

ListaDEC::~ListaDEC()
{
    //dtor
}

void ListaDEC::InsertarDEC(std::string nombre, std::string password) {

    NodoListaDEC *nuevo = new NodoListaDEC(nombre, password);
    //int numero_empleado = 1 + this->Tamanio;
    //std::string codigo = (numero_empleado < 100 ? (numero_empleado < 10 ? "SC-00"+std::to_string(numero_empleado) : "SC-0"+std::to_string(numero_empleado)): "SC-"+std::to_string(numero_empleado));
    //nuevo->EmpleadoSistema->Codigo = codigo;

    if (this->Primero == 0) { //Si la lista está vacía

        nuevo->Anterior = nuevo;
        nuevo->Siguiente = nuevo;

        this->Primero = nuevo;
        this->Tamanio++;


    } else {    // Si la lista NO está vacía

        NodoListaDEC *aux = this->Primero;
        int contador = 1;

        while (this->Tamanio > contador) {
            aux = aux->Siguiente;
            contador++;
        }

        nuevo->Anterior = aux;
        nuevo->Siguiente = this->Primero;
        aux->Siguiente = nuevo;
        this->Primero->Anterior = nuevo;
        this->Tamanio++;
    }
}

void ListaDEC::verListaDEC() {

    if (this->Primero == nullptr) {
        cout << "La lista está vacía." << endl;
        return;
    }

    NodoListaDEC *aux = this->Primero;
    int contador = 0;

    cout << "" << endl;
    cout << "**********       LISTADO DE EMPLEADOS      **********" << endl;
    cout << "  NOMBRE   /   CONTRASENA" << endl;

    do {
        std::cout << contador+1 << ". " << aux->EmpleadoSistema->Nombre << ", " << aux->EmpleadoSistema->Password << std::endl;
        aux = aux->Siguiente;
        contador++;

    } while (aux != this->Primero);

    cout << "" << endl;
}

void ListaDEC::leerArchivo(std::string nombre_archivo){
    try {
        ifstream lectura;
        lectura.open(nombre_archivo, ios::in);
        bool encabezado = false;

        for (std::string fila; std::getline(lectura, fila);) {
            std::stringstream lineas(fila);
            std::string nombre;
            std::string password;

            if (encabezado) {

                getline(lineas, nombre, ',');
                getline(lineas, password, ',');
                this->InsertarDEC(nombre, password);

            } else {

                encabezado = true;

            }
        }
    } catch (exception) {
        std::cout << "No se pudo leer el archivo" << std::endl;
    }
}

```
  
</details>

### Clase Tarea
La clase Tarea representa una tarea del sistema, y almacena información sobre la misma.

<details>
  <summary> Código </summary>
  <br>

``` C++
Tarea::Tarea(std::string codigo, std::string nombre_tarea, std::string codigo_encargado)
{
    this->Codigo = codigo;
    this->Nombre_Tarea = nombre_tarea;
    this->Codigo_Encargado = codigo_encargado;
}
```
</details>

### Clase Nodo Lista Doblemente Enlazada
La clase NodoListaDE es un nodo utilizado en la lista doblemente enlazada, y que almacena información sobre tareas.

Constructor NodoListaDE(std::string codigo, std::string nombre_tarea, std::string codigo_encargado): Este constructor crea un nodo en la lista doblemente enlazada para almacenar información sobre una tarea. Toma tres parámetros: codigo, nombre_tarea y codigo_encargado.

```this->Siguiente = 0;```: Inicializa el puntero Siguiente en nulo.  
```this->Anterior = 0;```: Inicializa el puntero Anterior en nulo.  
```this->TareaSistema = new Tarea(codigo, nombre_tarea, codigo_encargado);```: Crea un nuevo objeto Tarea utilizando los parámetros proporcionados y asigna este objeto al puntero TareaSistema del nodo.  

<details>
  <summary> Código </summary>
  <br>
``` C++
NodoListaDE::NodoListaDE(std::string codigo, std::string nombre_tarea, std::string codigo_encargado)
{
    this->Siguiente = 0;
    this->Anterior = 0;
    this->TareaSistema = new Tarea(codigo, nombre_tarea, codigo_encargado);
}
```
</details>

### Clase Lista Doblemente Enlazada
La clase ListaDE representa una lista doblemente enlazada que almacena la información de las tareas.

Constructor ```ListaDE()```: Inicializa la lista estableciendo el puntero Primero en nulo y el tamaño en 0.

Método ```InsertarDE(std::string codigo, std::string nombre_tarea, std::string codigo_encargado)```: Inserta un nuevo nodo en la lista con la información de la tarea proporcionada. Si la lista está vacía, el nuevo nodo se convierte en el primero. Si no está vacía, el nuevo nodo se agrega al final.

Método ```AsignarDE(std::string codigo, std::string nombre_tarea, std::string encargado)```: Busca una tarea por código y nombre en la lista y actualiza el código del encargado asignado a la tarea.

Método ```verListaDE()```: Muestra por consola los códigos, nombres de tarea y códigos de encargado de las tareas almacenadas en la lista.

<details>
  <summary> Código </summary>
  <br>
  
``` C++
  
#include "ListaDE.h"
#include <string>
#include <iostream>

using namespace std;

ListaDE::ListaDE()
{
    this->Primero = 0;
    this->Tamanio = 0;
}

ListaDE::~ListaDE()
{
    //dtor
}

void ListaDE::InsertarDE(std::string codigo, std::string nombre_tarea, std::string codigo_encargado) {

    NodoListaDE *nuevo = new NodoListaDE(codigo, nombre_tarea, codigo_encargado);

    if (this->Primero == 0) {

        this->Primero = nuevo;
        this->Tamanio++;

    } else {

        NodoListaDE *aux = this->Primero;

        while (aux->Siguiente) {

            aux = aux->Siguiente;

        }

        nuevo->Anterior = aux;
        aux->Siguiente = nuevo;
        this->Tamanio++;

    }

}

void ListaDE::AsignarDE(std::string codigo, std::string nombre_tarea, std::string encargado) {

    if (this->Primero) {

        NodoListaDE *aux = this->Primero;

        while(aux) {

            if (aux->TareaSistema->Codigo.compare(codigo) == 0 && aux->TareaSistema->Nombre_Tarea.compare(nombre_tarea)) {

                aux->TareaSistema->Codigo_Encargado = encargado;
                break;
            }
            aux = aux->Siguiente;
        }
    }
}
void ListaDE::verListaDE() {
    if (this->Primero == nullptr) {
        cout << "La lista está vacía." << endl;
        return;
    }
    NodoListaDE *aux = this->Primero;
    int contador = 0;

    cout << "" << endl;
    cout << "**********       LISTADO DE TAREAS        **********" << endl;
    cout << " CODIGO   /  NOMBRE   / ENCARGADO " << endl;

    while(aux){
        std::cout << contador+1 << ". " << aux->TareaSistema->Codigo << ", " << aux->TareaSistema->Nombre_Tarea << ", " << aux->TareaSistema->Codigo_Encargado << endl;
        aux = aux->Siguiente;
        contador++;
    }
    cout << "" << endl;
}

```
</details>

### Clase Proyecto
La clase Proyecto parece representa un proyecto en el sistema y almacena información relevante sobre este.  

Constructor Proyecto(std::string codigo, std::string nombre): Este constructor crea una instancia de la clase Proyecto. Toma dos parámetros: codigo y nombre.

```this->Nombre = nombre;```: Inicializa el atributo Nombre del proyecto con el valor proporcionado como parámetro.
```this->Codigo = codigo;```: Inicializa el atributo Codigo del proyecto con el valor proporcionado como parámetro.

<details>
  <summary> Código </summary>
  <br>
  
``` C++
Proyecto::Proyecto(std::string codigo, std::string nombre)
{
    this->Nombre = nombre;
    this->Codigo = codigo;
}
```
  
</details>

### Clase Nodo Cola
La clase NodoCola es un nodo utilizado en una cola de prioridad que almacena información sobre proyectos.

```Constructor NodoCola(Proyecto *nuevoProyecto, std::string prioridad)```: Este constructor crea un nodo en la cola de prioridad para almacenar información sobre un proyecto. Toma dos parámetros: nuevoProyecto, un puntero a un objeto Proyecto, y prioridad, una cadena que indica la prioridad del proyecto.

```this->Siguiente = 0;```: Inicializa el puntero Siguiente en nulo.
```this->Proyecto_C = nuevoProyecto;```: Asigna el puntero proporcionado nuevoProyecto al atributo Proyecto_C del nodo.
```this->Prioridad = prioridad;```: Inicializa el atributo Prioridad del nodo con la cadena proporcionada.

<details>
  <summary> Código </summary>
  <br>

``` C++
NodoCola::NodoCola(Proyecto *nuevoProyecto, std::string prioridad)
{
    this->Siguiente = 0;
    this->Proyecto_C = nuevoProyecto;
    this->Prioridad = prioridad;
}

```

</details>

### Clase Cola de Prioridad
La clase ColaPrioridad parece representar una cola de prioridad que almacena proyectos y los organiza según su prioridad. Aquí tienes una explicación resumida de sus métodos:

Constructor ```ColaPrioridad()```: Inicializa la cola de prioridad estableciendo el puntero Primero en nulo y el tamaño en 0.

Método ```Encolar(std::string Nombre, std::string Tipo_de_Prioridad)```: Agrega un nuevo proyecto a la cola con el nombre y la prioridad proporcionados. Crea un nuevo objeto de proyecto y nodo de cola, luego agrega el nodo a la cola.

Método ```VerProyectos()```: Muestra por consola los códigos, nombres de proyecto y prioridades de los proyectos en la cola.

Método ```Descolar()```: Elimina el proyecto en el frente de la cola (el de mayor prioridad) moviendo el puntero Primero al siguiente nodo.

Método ```Ordenar()```: Ordena los proyectos en la cola según su prioridad. Recorre la cola y realiza intercambios si la prioridad de un nodo es mayor que la del siguiente.

Método ```Graficar()```: Genera un archivo DOT para representar gráficamente la cola de prioridad y luego crea una imagen (formato JPG) utilizando el comando dot del sistema.

<details>
  <summary> Código </summary>
  <br>

``` C++

#include "ColaPrioridad.h"

ColaPrioridad::ColaPrioridad()
{
    this->Primero = 0;
    this->Tamanio = 0;
}

ColaPrioridad::~ColaPrioridad()
{
    //dtor
}

void ColaPrioridad::Encolar(std::string Nombre, std::string Tipo_de_Prioridad) {

    int numero_proyecto = 100 + this->Tamanio;
    Proyecto *nuevoProyecto = new Proyecto("PY-"+std::to_string(numero_proyecto),Nombre);
    NodoCola *nuevoNodo = new NodoCola(nuevoProyecto,Tipo_de_Prioridad);

    if (this->Primero == 0) {

        this->Primero = nuevoNodo;
        this->Tamanio++;

    } else {

        NodoCola *aux = this->Primero;

        while(aux->Siguiente){

            aux = aux->Siguiente;

        }

        aux->Siguiente = nuevoNodo;
        this->Tamanio++;

    }

}

void ColaPrioridad::VerProyectos()
{
    NodoCola *aux = this->Primero;
    int contador = 0;

    cout << "" << endl;
    cout << "**********     LISTADO DE PROYECTOS     **********" << endl;
    cout << " CODIGO  /  NOMBRE  / PRIORIDAD" << endl;

    while(aux)
    {
        cout << aux->Proyecto_C->Codigo << ", " << aux->Proyecto_C->Nombre << ", " << aux->Prioridad << endl;
        aux = aux->Siguiente;
        contador++;
    }

    cout << "" << endl;
}

void ColaPrioridad::Descolar()
{
    if(this->Primero)
    {
        this->Primero = this->Primero->Siguiente;
    }
}

void ColaPrioridad::Ordenar()
{
    if(this->Primero)
    {
        NodoCola *piv = this->Primero;
        NodoCola *actual;
        int contador = 0;
        while(contador != this->Tamanio)
        {
            actual = piv->Siguiente;
            while(actual)
            {
                if(piv->Prioridad.compare(actual->Prioridad) == 1)
                {
                    Proyecto *tempProyecto = piv->Proyecto_C;
                    std::string tempPrioridad = piv->Prioridad;
                    piv->Proyecto_C = actual->Proyecto_C;
                    piv->Prioridad = actual->Prioridad;
                    actual->Proyecto_C = tempProyecto;
                    actual->Prioridad = tempPrioridad;
                }
                actual = actual->Siguiente;
            }
            piv = piv->Siguiente;
            contador++;
        }
    }
}

void ColaPrioridad::Graficar(){
    ofstream arch;
    std::string text = "";
    std::string nombre_archivo = "cola.dot";
    std::string nombre_imagen = "cola.jpg";

    NodoCola *actual = Primero;

    arch.open(nombre_archivo, ios::out);
    if (actual != 0) {
        arch << "digraph G{\n node[shape=box]; rankdir=LR;\n";
        while (actual) {
            arch << "    \"" << actual->Proyecto_C->Codigo << "\" [label=\"" << actual->Proyecto_C->Codigo << "\\nPrioridad: " << actual->Prioridad << "\"];" << endl;
            if (actual->Siguiente) {
                arch << "    \"" << actual->Proyecto_C->Codigo << "\" -> \"" << actual->Siguiente->Proyecto_C->Codigo << "\";" << endl;
            }
            actual = actual->Siguiente;
        }

        arch << "}" << endl;
        arch.close();
    }
    std::string codigo_cmd = "dot -Tjpg ";
    codigo_cmd += nombre_archivo;
    codigo_cmd += " -o ";
    codigo_cmd += nombre_imagen;
    char j[codigo_cmd.size() + 1];
    strcpy(j, codigo_cmd.c_str());
    cout << j << endl;
    system(j);
}


```

</details>

### Clase Matriz
La clase Matriz parece ser una implementación de una matriz dispersa que almacena información relacionada con proyectos y empleados. Aquí está una explicación resumida de sus métodos:

Constructor Matriz(): Crea una matriz con un nodo raíz que actúa como una referencia inicial. Establece las coordenadas iniciales en 0.

Destructor ~Matriz(): Está vacío, no realiza ninguna acción especial en esta implementación.

Método buscarF(int y): Busca un nodo en la matriz por coordenada Y (fila). Recorre la columna de la matriz hasta encontrar el nodo correspondiente.

Método buscarC(int x): Busca un nodo en la matriz por coordenada X (columna). Recorre la fila de la matriz hasta encontrar el nodo correspondiente.

Método insertar_columna(NodoMatriz *nuevo, NodoMatriz *cabeza_columna): Inserta un nuevo nodo columna en la matriz. Recorre la fila para encontrar la posición correcta y realiza la inserción.

Método insertar_fila(NodoMatriz *nuevo, NodoMatriz *cabeza_fila): Inserta un nuevo nodo fila en la matriz. Recorre la columna para encontrar la posición correcta y realiza la inserción.

Método ```nueva_columna_1(int x, Proyecto *proyecto)```: Crea un nuevo nodo columna y lo inserta en la matriz.

Método ```insertar_proyecto(ColaPrioridad *cola)```: Inserta un proyecto en la matriz en una nueva columna.

Método ```nueva_fila_1(int y, Empleado *encargado)```: Crea un nuevo nodo fila y lo inserta en la matriz.

Método ```insertar_empleado(ListaDEC *lista)```: Inserta empleados en la matriz en nuevas filas.

Método ```asignarProyecto(std::string nombre_empleado, std::string codigo_proyecto)```: Asigna un proyecto a un empleado en la matriz.

Método ```buscarF_1(std::string nombre)```: Busca un nodo fila en la matriz por nombre de empleado.

Método ```buscarC_1(std::string codigo)```: Busca un nodo columna en la matriz por código de proyecto.

Método ```BuscarProyecto(std::string codigo, std::string nombre_tarea)```: Busca un proyecto en la matriz por código y agrega una tarea a él.

Método ```BuscarEmpleado(std::string codigo, std::string nombre_tarea, std::string nombre_empleado)```: Busca un empleado en la matriz y asigna una tarea a él.

Método ```Graficar()```: Genera un archivo DOT para representar gráficamente la matriz y luego crea una imagen (formato JPG) utilizando el comando dot del sistema.

<details>
  <summary> Código </summary>
  <br>

``` C++

#include "Matriz.h"

Matriz::Matriz()
{
    this->Raiz = new NodoMatriz(new Proyecto("RAIZ",""),new Empleado("",""),-1,-1);
    this->CoordenadaX = 0;
    this->CoordenadaY = 0;
}

Matriz::~Matriz()
{
    //dtor
}

NodoMatriz* Matriz::buscarF(int y)
{
    NodoMatriz *aux = this->Raiz;
    while(aux != 0)
    {
        if(aux->PosY == y){

            return aux;

        }
        aux = aux->Abajo;
    }
    return 0;
}

NodoMatriz* Matriz::buscarC(int x)
{
    NodoMatriz *aux = this->Raiz;
    while(aux != 0) {

        if(aux->PosX == x) {

            return aux;

        }
        aux = aux->Siguiente;
    }
    return 0;
}

NodoMatriz* Matriz::insertar_columna(NodoMatriz *nuevo, NodoMatriz *cabeza_columna)
{
    NodoMatriz *temp = cabeza_columna;
    bool piv = false;
    while(true)
    {
        if(temp->PosX==nuevo->PosX){

            temp->PosY = nuevo->PosY;
            temp->Encargado_c = nuevo->Encargado_c;
            temp->Proyecto_c = nuevo->Proyecto_c;
            return temp;

        }else if(temp->PosX > nuevo->PosX){

            piv=true;
            break;

        }
        if (temp->Siguiente) {
            temp = temp->Siguiente;
        } else {
            break;
        }
    }

    if(piv)
        {
        nuevo->Siguiente = temp;
        temp->Anterior->Siguiente = nuevo;
        nuevo->Anterior=temp->Anterior;
        temp->Anterior=nuevo;

    } else {
        temp->Siguiente=nuevo;
        nuevo->Anterior=temp;
    }
    return nuevo;
}

NodoMatriz* Matriz::insertar_fila(NodoMatriz *nuevo, NodoMatriz *cabeza_fila)
{
    NodoMatriz *temp = cabeza_fila;
    bool piv = false;
    while(true) {

        if(temp->PosY==nuevo->PosY){

            temp->PosX = nuevo->PosX;
            temp->Encargado_c = nuevo->Encargado_c;
            temp->Proyecto_c = nuevo->Proyecto_c;
            return temp;

        } else if(temp->PosY > nuevo->PosY){

            piv=true;
            break;

        } if(temp->Abajo){

            temp = temp->Abajo;

        }else{

            break;

        }
    }
    if(piv) {

        nuevo->Abajo = temp;
        temp->Arriba->Abajo = nuevo;
        nuevo->Arriba = temp->Arriba;
        temp->Arriba = nuevo;

    } else {

        temp->Abajo = nuevo;
        nuevo->Arriba = temp;

    }

    return nuevo;
}

NodoMatriz* Matriz::nueva_columna_1(int x, Proyecto *proyecto){

    NodoMatriz *columna = this->insertar_columna(new NodoMatriz(proyecto, 0, x, -1), this->Raiz);
    return columna;
}

void Matriz::insertar_proyecto(ColaPrioridad *cola){

    NodoMatriz *nodo_Columna = this->nueva_columna_1(this->CoordenadaX, cola->Primero->Proyecto_C);
    this->CoordenadaX++;
}

NodoMatriz* Matriz::nueva_fila_1(int y, Empleado *encargado){

    NodoMatriz *fila = this->insertar_fila(new NodoMatriz(0, encargado, -1, y), this->Raiz);
    return fila;
}

void Matriz::insertar_empleado(ListaDEC *lista) {
    //
    NodoListaDEC *aux = lista->Primero;
    int contador = 0;
    while(lista->Tamanio > contador) {

        this->nueva_fila_1(this->CoordenadaY, aux->EmpleadoSistema);
        aux = aux->Siguiente;
        contador++;
        this->CoordenadaY++;
    }
}

void Matriz::asignarProyecto(std::string nombre_empleado, std::string codigo_proyecto) {

    NodoMatriz *nodo_Columna =  this->buscarC_1(codigo_proyecto);
    NodoMatriz *nodo_Fila = this->buscarF_1(nombre_empleado);

    NodoMatriz *nuevo = new NodoMatriz(nodo_Columna->Proyecto_c, nodo_Fila->Encargado_c, nodo_Columna->PosX, nodo_Fila->PosY);

    if(nodo_Columna != 0 && nodo_Fila !=0 ){

        nuevo=this->insertar_columna(nuevo, nodo_Fila);
        nuevo=this->insertar_fila(nuevo, nodo_Columna);
        return;

    } else {

        cout << "Se podrujo un error al insertar el nuevo nodo" << endl;

    }
}

NodoMatriz* Matriz::buscarF_1(std::string nombre) {

    NodoMatriz *aux = this->Raiz;
    while(aux != 0) {

        if(aux->Encargado_c->Nombre.compare(nombre) == 0) {

            return aux;
        }
        aux = aux->Abajo;
    }
    return 0;
}

NodoMatriz* Matriz::buscarC_1(std::string codigo) {

    NodoMatriz *aux = this->Raiz;
    while(aux != 0) {

        if(aux->Proyecto_c->Codigo.compare(codigo) == 0) {

            return aux;
        }
        aux = aux->Siguiente;
    }
    return 0;
}

void Matriz::BuscarProyecto(std::string codigo, std::string nombre_tarea) {

    NodoMatriz *nodo_Columna =  this->buscarC_1(codigo);
    nodo_Columna->Tareas->InsertarDE(codigo, nombre_tarea, "");
}

void Matriz::BuscarEmpleado(std::string codigo, std::string nombre_tarea, std::string nombre_empleado)
{
    NodoMatriz *nodo_Columna =  this->buscarC_1(codigo);
    NodoMatriz *nodo_Fila = this->buscarF_1(nombre_empleado);
    if(nodo_Fila != 0) {

        nodo_Columna->Tareas->AsignarDE(nodo_Columna->Proyecto_c->Codigo, nombre_tarea, nodo_Fila->Encargado_c->Codigo);

    } else {

        cout << "No hay empleado con ese nombre" << endl;

    }
}

void Matriz::Graficar() {

    ofstream archivo;
    std::string texto = "";
	std::string nombre_archivo = "matriz.dot";
	std::string nombre_imagen = "matriz.jpg";

	NodoMatriz *aux1 = this->Raiz;
	NodoMatriz *aux2 = this->Raiz;
	NodoMatriz *aux3 = this->Raiz;

	archivo.open(nombre_archivo, ios::out);

	if ( aux1 != 0 ) {
		archivo << "digraph MatrizCapa{ \n node[shape=box] \n rankdir=UD;\n";
        /** Creacion de los nodos actuales */
        /*while( aux1 != 0 ) {
            archivo << "nodo" << (aux1->PosX+1) << (aux1->PosY+1) << "[label=\"" << aux1->Proyecto << "\" ,rankdir=LR,group=" << (aux1->PosX+1) << "]; \n";
            aux1 = aux1->Siguiente;
        }
        archivo << "}";*/
        while( aux2 != 0 ) {
            aux1 = aux2;
            archivo << "{rank=same; \n";
            while( aux1 != 0 ) {
                if(aux1->Proyecto_c)
                    {
                    if(aux1->Encargado_c) {

                        archivo << "nodo" << aux1 << "[label=\"" << aux1->Proyecto_c->Codigo << "\\n" << aux1->Encargado_c->Codigo << "\" ,group=" << (aux1->PosX+1) << "]; \n";

                    }else{

                        archivo << "nodo" << aux1 << "[label=\"" << aux1->Proyecto_c->Codigo << "\" ,group=" << (aux1->PosX+1) << ", style=filled, fillcolor=\"lightblue\"];\n";

                    }

                } else if(aux1->Encargado_c) {
                    archivo << "nodo" << aux1 << "[label=\"" << aux1->Encargado_c->Nombre << "\" ,group=" << (aux1->PosX+1) << ", style=filled, fillcolor=\"orange\"];\n";
                }
                aux1 = aux1->Siguiente;
            }
            archivo << "} \n";
            aux2 = aux2->Abajo;
        }
        /** Conexiones entre los nodos de la matriz */
        aux2 = aux3;
        while( aux2 != 0 ) {
            aux1 = aux2;
            while( aux1->Siguiente != 0 ) {
                archivo << "nodo" << aux1 << " -> " << "nodo" << aux1->Siguiente << " [dir=both];\n";
                aux1 = aux1->Siguiente;
            }
            aux2 = aux2->Abajo;
        }
        aux2 = aux3;
        while( aux2 != 0 ) {
            aux1 = aux2;
            while( aux1->Abajo != 0 ) {
                archivo << "nodo" << aux1 << " -> " << "nodo" << aux1->Abajo << " [dir=both];\n";
                aux1 = aux1->Abajo;
            }
            aux2 = aux2->Siguiente;
        }
        archivo << "} \n";
	} else {
		texto = "No hay elementos en la matriz";
	}

	archivo.close();
    std::string codigo_cmd="dot -Tjpg ";
    codigo_cmd+=nombre_archivo;
    codigo_cmd+=" -o ";
    codigo_cmd+=nombre_imagen;
    char j[codigo_cmd.size()+1];
    strcpy(j,codigo_cmd.c_str());
    cout << j << endl;
    system(j);
}


```
</details>
