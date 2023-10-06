#ifndef COLAPRIORIDAD_H
#define COLAPRIORIDAD_H

#include "NodoCola.h"
#include "Proyecto.h"

#include <string>
#include <iostream>

using namespace std;

class ColaPrioridad
{
    public:
        NodoCola *Primero;
        int Tamanio;
        void Encolar(std::string Nombre, std::string Tipo_de_Prioridad);
        void Descolar();
        void VerProyectos();
        void Ordenar();
        ColaPrioridad();
        virtual ~ColaPrioridad();

    protected:

    private:
};

#endif // COLAPRIORIDAD_H
