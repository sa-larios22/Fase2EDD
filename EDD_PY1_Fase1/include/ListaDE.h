#ifndef LISTADE_H
#define LISTADE_H

#include "NodoListaDE.h"
#include <string>

class ListaDE
{
    public:

        NodoListaDE *Primero;
        int Tamanio;

        void InsertarDE(std::string codigo, std::string nombre_tarea, std::string codigo_encargado);
        void AsignarDE(std::string codigo, std::string nombre_tarea, std::string encargado);
        void verListaDE();

        ListaDE();
        virtual ~ListaDE();

    protected:

    private:
};

#endif // LISTADE_H
