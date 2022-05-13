import math as mt
class Viaje():
    def __init__(self, origen, destino, distancia=None):
        self.origen=origen
        self.destino=destino
        self.distancia=distancia

    def Distancia(self, origen, destino):
        distancias=[]
        distancias[0]=(destino[0]+origen[0])/2
        distancias[1] = (destino[1] + origen[1]) / 2
        self.distancia=mt.sqrt(pow(distancias[0],2)+pow(distancias[1],2))
        return self.distancia

    def agregar_Viaje(self, origen, destino, viajes):
        distancia=self.Distancia(origen, destino)
        viajes.append([origen, destino, distancia])

    def Short_viaje(self, viajes):
        min_distancia=10000000
        for i in range(len(viajes)):
            if viajes[i][2]<min_distancia:
                min_distancia=viajes[i][2]
        return min_distancia

viajes=[]


