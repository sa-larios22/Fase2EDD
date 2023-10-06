#include "Proyecto.h"

Proyecto::Proyecto(std::string codigo, std::string nombre)
{
    this->Nombre = nombre;
    this->Codigo = codigo;
}

Proyecto::~Proyecto()
{
    //dtor
}
