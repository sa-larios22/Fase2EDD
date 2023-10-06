#include "NodoListaDEC.h"

NodoListaDEC::NodoListaDEC(std::string nombre, std::string password)
{
    this->Siguiente = 0;
    this->Anterior = 0;
    this->EmpleadoSistema = new Empleado(nombre, password);
}

NodoListaDEC::~NodoListaDEC()
{
    //dtor
}
