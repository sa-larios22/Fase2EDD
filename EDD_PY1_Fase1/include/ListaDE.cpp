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
