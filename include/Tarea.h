#ifndef TAREA_H
#define TAREA_H

#include <string>

class Tarea
{
    public:

        std::string Codigo;
        std::string Nombre_Tarea;
        std::string Codigo_Encargado;

        Tarea(std::string codigo, std::string nombre_tarea, std::string codigo_encargado);
        virtual ~Tarea();

    protected:

    private:
};

#endif // TAREA_H
