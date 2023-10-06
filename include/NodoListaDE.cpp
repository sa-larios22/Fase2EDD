#include "NodoListaDE.h"

NodoListaDE::NodoListaDE(std::string codigo, std::string nombre_tarea, std::string codigo_encargado)
{
    this->Siguiente = 0;
    this->Anterior = 0;
    this->TareaSistema = new Tarea(codigo, nombre_tarea, codigo_encargado);
}

NodoListaDE::~NodoListaDE()
{
    //dtor
}
