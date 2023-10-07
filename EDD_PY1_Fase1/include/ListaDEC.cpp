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
