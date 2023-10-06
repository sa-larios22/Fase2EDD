#include "ColaPrioridad.h"

ColaPrioridad::ColaPrioridad()
{
    this->Primero = 0;
    this->Tamanio = 0;
}

ColaPrioridad::~ColaPrioridad()
{
    //dtor
}

void ColaPrioridad::Encolar(std::string Nombre, std::string Tipo_de_Prioridad) {

    int numero_proyecto = 100 + this->Tamanio;
    Proyecto *nuevoProyecto = new Proyecto("PY-"+std::to_string(numero_proyecto),Nombre);
    NodoCola *nuevoNodo = new NodoCola(nuevoProyecto,Tipo_de_Prioridad);

    if (this->Primero == 0) {

        this->Primero = nuevoNodo;
        this->Tamanio++;

    } else {

        NodoCola *aux = this->Primero;

        while(aux->Siguiente){

            aux = aux->Siguiente;

        }

        aux->Siguiente = nuevoNodo;
        this->Tamanio++;

    }

}

void ColaPrioridad::VerProyectos()
{
    NodoCola *aux = this->Primero;
    int contador = 0;

    cout << "" << endl;
    cout << "**********     LISTADO DE PROYECTOS     **********" << endl;
    cout << " CODIGO  /  NOMBRE  / PRIORIDAD" << endl;

    while(aux)
    {
        cout << aux->Proyecto_C->Codigo << ", " << aux->Proyecto_C->Nombre << ", " << aux->Prioridad << endl;
        aux = aux->Siguiente;
        contador++;
    }

    cout << "" << endl;
}

void ColaPrioridad::Descolar()
{
    if(this->Primero)
    {
        this->Primero = this->Primero->Siguiente;
    }
}

void ColaPrioridad::Ordenar()
{
    if(this->Primero)
    {
        NodoCola *piv = this->Primero;
        NodoCola *actual;
        int contador = 0;
        while(contador != this->Tamanio)
        {
            actual = piv->Siguiente;
            while(actual)
            {
                if(piv->Prioridad.compare(actual->Prioridad) == 1)
                {
                    Proyecto *tempProyecto = piv->Proyecto_C;
                    std::string tempPrioridad = piv->Prioridad;
                    piv->Proyecto_C = actual->Proyecto_C;
                    piv->Prioridad = actual->Prioridad;
                    actual->Proyecto_C = tempProyecto;
                    actual->Prioridad = tempPrioridad;
                }
                actual = actual->Siguiente;
            }
            piv = piv->Siguiente;
            contador++;
        }
    }
}
