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
