import math as mt
import time
from math import acos, cos, sin, radians
from arbol_BST import BST

#Estructuras de datos
from src.src_package import arbol_BST


class Nodo():
    def __init__(self, dato=None, next=None):
        self.dato=dato
        self.next=next

class Cola_nodo():
    def __init__(self):
        self.len_cola=0
        self.front=None
        self.rear=None

    def empty(self):
        return self.len_cola == 0

    def enqueue(self, dato):
        nodo=Nodo(dato)
        nodo.next=None
        if self.len_cola == 0:
            self.front=self.rear=nodo
        else:
            rear=self.rear
            rear.next=nodo
            self.rear=nodo
        self.len_cola+=1


    def dequeue(self):
        dato=self.front.dato
        self.front=self.front.next
        self.len_cola -= 1
        if self.len_cola==0:
            self.rear=None
        return dato


    def front(self):
        return self.front.dato

    def print_list(self):
        node = self.front
        while node != None:
            print(node.dato)
            node = node.next

class Cola_arreglo:
    def __init__(self):
        self.count = 0
        self.arr = []
        self.size = 10 #este atributo se debe cambiar con cada implementación
        self.top = 0
        self.tail = 0
    
    def enqueue(self,data):
        if self.full() is False:
            self.arr.append(data)
            self.count+=1
            self.tail = (self.tail+1)%self.size
        else: #este else se debe cambiar con cada implementación
            self.dequeue()
            self.enqueue(data)
    
    def dequeue(self):
        if self.empty() is False:
            self.arr.remove(self.arr[0])
            self.count-=1
            self.top = (self.top+1)%self.size
        else:
            print('Cola vacia')
    
    def empty(self):
        return self.count == 0
    
    def full(self):
        return self.count >= self.size
    
    #este método se modificó del original
    def output(self):
        for elemento in self.arr:
            print(elemento)

#clases
class Edificio():
    def __init__(self, nombre_edificio=None, num_edificio=None, coordenadas=None):
        self.nombre_edificio=nombre_edificio
        self.num_edificio=num_edificio
        self.coordenadas=coordenadas

class Viaje():
    #constructor de la clase. Recibe como parámetros el origen y el destino del viaje.
    def __init__(self, origen, destino):
        self.origen=origen
        self.destino=destino
        

    #método que calcula la distancia entre dos puntos a partir de las coordenadas (latitud, longitud)
    def distancia_puntos(self):
        origen = (radians(self.origen.coordenadas[0]), radians(self.origen.coordenadas[1]))
        destino = (radians(self.destino.coordenadas[0]), radians(self.destino.coordenadas[1]))
        distancia = acos(sin(origen[0])*sin(destino[0]) + cos(origen[0])*cos(destino[0])*cos(origen[1] - destino[1]))
        return round(distancia*6371.01*1000,2) # retorna distancia en metros

    #método que calcula la distancia y va almacenando en el historial los nombres de los edificios de origen y destino, así como la distancia entre estos.
    def hacer_viaje(self):
        distancia=self.distancia_puntos()
        nombre_edificio_origen=self.origen.nombre_edificio
        nombre_edificio_destino=self.destino.nombre_edificio

        #segmento de código para agregar al historial cola como lista.
        #<<<<<<<<<<<<<<<<<<<<
        if historial_general.len_cola<10:
            historial_general.enqueue([nombre_edificio_origen, nombre_edificio_destino, distancia])
        else:
            historial_general.dequeue()
            historial_general.enqueue([nombre_edificio_origen, nombre_edificio_destino, distancia])
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        #segmento de código para agregar al historial cola como arreglo.
        #<<<<<<<<<<<<<<<<<<<
            #historial_general.enqueue([nombre_edificio_origen, nombre_edificio_destino, distancia])
        #>>>>>>>>>>>>>>>>>>>>>>>


    def short_viaje(self, viajes):
        min_distancia=10000000
        for i in range(len(viajes)):
            if viajes[i][2]<min_distancia:
                min_distancia=viajes[i][2]
        return min_distancia

#clase historial. Hereda de cola_nodo
class Historial(Cola_nodo):
    def __init__(self):
        Cola_nodo.__init__(self)

#clase historial. Hereda de cola_arreglo (falta sobreescribir los métodos originales de cola_arreglo de acuerdo con las necesidades propias del historial [tamaño, dequeue/enqueue])
"""
class Historial(Cola_arreglo):
    def __init__(self):
        Cola_arreglo.__init__(self)"""


#Entry point
if __name__ == '__main__':
    #se instancia el historial. Solo será uno.

    historial_general = Historial()

    edificios=[Edificio("Yu Takeuchi", 404, [4.637574, -74.082677]), Edificio("CyT", 454, [4.638007, -74.084678]),
    Edificio("León de Greiff", 104, [4.635576, -74.082589]),
    Edificio("Biblioteca Gabriel García Márquez", 102, [4.635416, -74.082997]),
    Edificio("Edificio Julio Garavito Armero - Facultad de Ingeniería", 401, [4.637304, -74.082760])]

    arbol_edificios=arbol_BST.BST()
    for i in range(len(edificios)):
        arbol_edificios.BST_insert(edificios[i].num_edificio)
        print(edificios[i].num_edificio)


    '''viaje1 = Viaje(edificio1, edificio2)
    viaje2 = Viaje(edificio2, edificio1)
    viaje3 = Viaje(edificio4, edificio2)
    viaje4 = Viaje(edificio1, edificio5)
    viaje5 = Viaje(edificio3, edificio2)
    viaje6 = Viaje(edificio1, edificio3)
    viaje7 = Viaje(edificio5, edificio4)
    viaje8 = Viaje(edificio1, edificio3)
    viaje9 = Viaje(edificio4, edificio2)
    viaje10 = Viaje(edificio5, edificio3)
    #viaje10 = Viaje(edificio4, edificio1)
    viaje1.hacer_viaje()
    viaje2.hacer_viaje()
    viaje3.hacer_viaje()
    viaje4.hacer_viaje()
    viaje5.hacer_viaje()
    viaje6.hacer_viaje()
    viaje7.hacer_viaje()
    viaje8.hacer_viaje()
    viaje9.hacer_viaje()
    viaje10.hacer_viaje()
    #viaje11.hacer_viaje()'''

    historial_general.print_list()