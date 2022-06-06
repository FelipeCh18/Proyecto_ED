from math import acos, cos, sin, radians

#Estructuras de datos
import unicodedata

from src.src_package.estructuras import arbol_BST

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
    origen=int(input())
    destino=int(input())

    historial_general = Historial()

    edificios=[Edificio("Departamento de Farmacia", 450, [4.6372861417941635, -74.0834874406681]),
                Edificio("Departamento de Química", 451, [4.637764685367428, -74.0835330382217]),
                Edificio("Talleres de Mantenimiento", 435, [4.64205482639357, -74.08360455507342]),
                Edificio("Capilla", 251, [4.632884886630808, -74.08151230506716]),
                Edificio("Instituto Pedagógico Arturo Ramírez Montúfar IPARM", 434, [4.641252188515629, -74.08342681259816]),
                Edificio("Aulas de Ingeniería", 453, [4.638454429180191, -74.08373152169051]),
                Edificio("Museo de Arquitectura Leopoldo Rother", 207, [4.634041664995465, -74.0832540028815]),
                Edificio("Postgrados de Ciencias Económicas", 238, [4.6326404471845875, -74.08322608296592]),
                Edificio("Instituto de Ciencias Naturales", 425, [4.6422771700375804, -74.0819424605535]),
                Edificio("Postgrados en Arquitectura - SINDU", 314, [4.635824135627152, -74.08066504067277]),
                Edificio("Edificio Orlando Fals Borda: Departamento de Sociología", 205, [4.634452309547205, -74.08387430410457]),
                Edificio("Edificio Francisco de Paula Santander: Diseño Gráfico", 217, [4.633585502038007, -74.08328479644659]),
                Edificio("Banco Popular", 230, [4.632901877394506, -74.08477948528329]),
                Edificio("Facultad de Medicina", 471, [4.6364119300590705, -74.08442889603137]),
                Edificio("Departamento de Lenguas Extranjeras", 229, [4.632726658071325, -74.08451861259083]),
                Edificio("Portería Peatonal Calle 26", 235, [4.632525465261985, -74.08392775782852]),
                Edificio("Canchas de Tenis T-2, T-3 y T-4", 414, [4.639525444501469, -74.08367406073157]),
                Edificio("Laboratorio de Ensayos Hidráulicos", 408, [4.63821149349025, -74.08149173609216]),
                Edificio("Parque Automotor", 436, [4.641669240925287, -74.08348313898786]),
                Edificio("Postgrados en Materiales y Procesos de Manufactura", 407, [4.639263646631807, -74.0822111001772]),
                Edificio("Edificio Antonio Nariño - Departamento de Lingüistica. Departamento de Ingeniería Civil y Agrícola.", 214, [4.633455840055661, -74.084017710065]),
                Edificio("Facultad de Enfermería (Nuevo)", 228, [4.635232340842952, -74.08494106051288]),
                Edificio("Restaurante 'Campus' de Ciencias Humanas", 213, [4.633767964486836, -74.08430738863912]),
                Edificio("León de Greiff", 104, [4.635679915166562, -74.08233173656821]),
                Edificio("Torre de Enfermería", 101, [4.635168159913767, -74.08241720288407]),
                Edificio("Centro de Acopio de Residuos Sólidos", 437, [4.641302342792041, -74.08397457887394]),
                Edificio("Almacén e Imprenta", 433, [4.641166639263639, -74.08353141874946]),
                Edificio("Instituto de Extensión e Investigación - IEI", 406, [4.638256683909461, -74.08243470824875]),
                Edificio("Escuela de Artes Plásticas", 301, [4.6363116622260225, -74.08221569333892]),
                Edificio("Facultad de Odontología", 210, [4.634559664993099, -74.08522267343369]),
                Edificio("Perrera", 473, [4.63521513758165, -74.08591928063423]),
                Edificio("Instituto de Genética", 426, [4.642876013587281, -74.08300595643392]),
                Edificio("Portería Acceso Vehicular Capilla", 252, [4.632485465444149, -74.08164199400272]),
                Edificio("Edificio Rogelio Salmona de Postgrados en Ciencias Humanas", 225, [4.63428460696461, -74.08655977365419]),
                Edificio("Departamento de Biología", 421, [4.640461140973933, -74.08188636841575]),
                Edificio("Facultad de Derecho, Ciencias Politicas y Sociales", 201, [4.635419923588457, -74.08383511471597]),
                Edificio("Laboratorios de Ingeniería Química", 412, [4.6389666994381455, -74.083267706068]),
                Edificio("Polideportivo", 103, [4.634831099102443, -74.0829975949591]),
                Edificio("Edificio Ciencia y Tecnología - CyT", 454, [4.63805341542632, -74.08471321019677]),
                Edificio("Museo de Arte", 317, [4.634562273519589, -74.08083133763094]),
                Edificio("Biblioteca Gabriel García Márquez", 102, [4.635317306785998, -74.0832505028769]),
                Edificio("Cafetería de Odontología", 211, [4.63436948868896, -74.08547414956642]),
                Edificio("Escuela de Arquitectura", 303, [4.636736734275307, -74.08160415237948]),
                Edificio("Dirección Nacional de Innovación Académica", 477, [4.636864549649436, -74.08534437211763]),
                Edificio("Instituto Pedagógico Arturo Ramírez Montúfar: IPARM", 431, [4.6410794814153045, -74.08282490732093]),
                Edificio("Postgrados en Bioquímica y Carbones", 452, [4.63711771576264, -74.08447985800483]),
                Edificio("Postgrados en Matemáticas y Física", 405, [4.637758348985364, -74.08172452460337]),
                Edificio("Laboratorio de Hidráulica", 409, [4.638559056536617, -74.0817897627584]),
                Edificio("Portería Salida Vehicular Capilla", 253, [4.633450579117872, -74.08073540735573]),
                Edificio("Edificio Julio Garavito Armero - Facultad de Ingeniería", 401, [4.637304, -74.082760]),
                Edificio("Laboratorios de Ingeniería", 411, [4.639156512406468, -74.08260117712538]),
                Edificio("Bloque II Facultad de Ciencias Económicas", 311, [4.637604640600882, -74.08095740145617]),
                Edificio("Conservatorio de Música", 305, [4.635571117486736, -74.08117231672759]),
                Edificio("Edificio Manuel Ancízar", 224, [4.634000553899457, -74.0860850226576]),
                Edificio("Talleres y Aulas de Construcción", 309, [4.6364961955953, -74.08063562901637]),
                Edificio("Facultad de Ciencias Económicas", 310, [4.637211338202991, -74.08076236339367]),
                Edificio("Aulas de Ciencias Humanas", 212, [4.634068726652622, -74.08467820403695]),
                Edificio("Facultad de Ciencias", 476, [4.637287619874028, -74.08552072736123]),
                Edificio("Filosofía", 239, [4.6323455717377335, -74.08331072877552]),
                Edificio("Edificio Yu Takeuchi - Departamentos de Matemáticas, Física y Estadística", 404, [4.637574, -74.082677]),
                Edificio("Observatorio Astronómico", 413, [4.639806153566646, -74.08336158338332])]
    
    Edificios_Nombre = []
    Edificios_Numero = []

    for i in edificios:
        Edificios_Nombre.append(unicodedata.normalize('NFKD', i.nombre_edificio).encode('ASCII', 'ignore').lower())
        Edificios_Numero.append(str(i.num_edificio))

    arbol_edificios= arbol_BST.BST()
    for i in range(len(edificios)):
        arbol_edificios.BST_insert(edificios[i])

    ori=arbol_edificios.find(origen, arbol_edificios.root)
    dest=arbol_edificios.find(destino, arbol_edificios.root)

    viaje1 = Viaje(ori, dest)
    viaje1.hacer_viaje()
    historial_general.print_list()

    '''viaje2 = Viaje(edificio2, edificio1)
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

