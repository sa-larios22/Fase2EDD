#include "NodoCola.h"

NodoCola::NodoCola(Proyecto *nuevoProyecto, std::string prioridad)
{
    this->Siguiente = 0;
    this->Proyecto_C = nuevoProyecto;
    this->Prioridad = prioridad;
}

NodoCola::~NodoCola()
{
    //dtor
}
