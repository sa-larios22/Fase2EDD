#ifndef NODOLISTADE_H
#define NODOLISTADE_H

#include "Tarea.h"

class NodoListaDE
{
    public:

        Tarea *TareaSistema;
        NodoListaDE *Siguiente;
        NodoListaDE *Anterior;

        NodoListaDE(std::string codigo, std::string nombre_tarea, std::string codigo_encargado);
        virtual ~NodoListaDE();

    protected:

    private:
};

#endif // NODOLISTADE_H
