#ifndef NODOLISTADEC_H
#define NODOLISTADEC_H

#include "Empleado.h"

class NodoListaDEC
{
    public:

        Empleado *EmpleadoSistema;
        NodoListaDEC *Siguiente;
        NodoListaDEC *Anterior;

        NodoListaDEC(std::string nombre, std::string password);
        virtual ~NodoListaDEC();

    protected:

    private:
};

#endif // NODOLISTADEC_H
