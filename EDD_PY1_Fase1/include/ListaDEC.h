#ifndef LISTADEC_H
#define LISTADEC_H

#include "NodoListaDEC.h"
#include <string>
#include <iostream>
#include <fstream>
#include <string.h>
#include <cstring>
#include <sstream>
#include <stdlib.h>

using namespace std;

class ListaDEC
{
    public:
        NodoListaDEC *Primero;
        int Tamanio;
        void InsertarDEC(std::string nombre, std::string password);
        void verListaDEC();
        void leerArchivo(std::string nombre_archivo);

        ListaDEC();
        virtual ~ListaDEC();

    protected:

    private:
};

#endif // LISTADEC_H
