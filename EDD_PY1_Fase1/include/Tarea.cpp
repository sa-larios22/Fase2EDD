#include "Tarea.h"

Tarea::Tarea(std::string codigo, std::string nombre_tarea, std::string codigo_encargado)
{
    this->Codigo = codigo;
    this->Nombre_Tarea = nombre_tarea;
    this->Codigo_Encargado = codigo_encargado;
}

Tarea::~Tarea()
{
    //dtor
}
