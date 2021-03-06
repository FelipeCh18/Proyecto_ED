from time import time
from math import acos, cos, sin, radians
from turtle import clear

# Estructuras de datos
import unicodedata

from estructuras import arbol_BST
from estructuras import Grafos
from estructuras.Grafos import dijkstra, shortest
from estructuras.Grafos import dijkstra_algorithm

class Nodo():
    def __init__(self, dato=None, next=None):
        self.dato = dato
        self.next = next

class Cola_nodo():
    def __init__(self):
        self.len_cola = 0
        self.front = None
        self.rear = None

    def empty(self):
        return self.len_cola == 0

    def enqueue(self, dato):
        nodo = Nodo(dato)
        nodo.next = None
        if self.len_cola == 0:
            self.front = self.rear = nodo
        else:
            rear = self.rear
            rear.next = nodo
            self.rear = nodo
        self.len_cola += 1

    def dequeue(self):
        dato = self.front.dato
        self.front = self.front.next
        self.len_cola -= 1
        if self.len_cola == 0:
            self.rear = None
        return dato

    def front(self):
        return self.front.dato

    def print_list(self):
        node = self.front
        while node != None:
            print(node.dato)
            node = node.next

# clases
class Edificio():
    def __init__(self, nombre_edificio=None, num_edificio=None, coordenadas=None):
        self.nombre_edificio = nombre_edificio
        self.num_edificio = num_edificio
        self.coordenadas = coordenadas

class Viaje():
    # constructor de la clase. Recibe como parámetros el origen y el destino del viaje.
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

    # método que calcula la distancia entre dos puntos a partir de las coordenadas (latitud, longitud)
    def distancia_puntos(self):
        origen = (radians(self.origen.coordenadas[0]), radians(self.origen.coordenadas[1]))
        destino = (radians(self.destino.coordenadas[0]), radians(self.destino.coordenadas[1]))
        distancia = acos(
            sin(origen[0]) * sin(destino[0]) + cos(origen[0]) * cos(destino[0]) * cos(origen[1] - destino[1]))
        return round(distancia * 6371.01 * 1000, 2)  # retorna distancia en metros

    # método que calcula la distancia y va almacenando en el historial los nombres de los edificios de origen y destino, así como la distancia entre estos.
    def hacer_viaje(self):
        distancia = self.distancia_puntos()
        nombre_edificio_origen = self.origen.nombre_edificio
        nombre_edificio_destino = self.destino.nombre_edificio

        # segmento de código para agregar al historial cola como lista.
        # <<<<<<<<<<<<<<<<<<<<
        if historial_general.len_cola < 10:
            historial_general.enqueue([nombre_edificio_origen, nombre_edificio_destino, distancia])
        else:
            historial_general.dequeue()
            historial_general.enqueue([nombre_edificio_origen, nombre_edificio_destino, distancia])
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # segmento de código para agregar al historial cola como arreglo.
        # <<<<<<<<<<<<<<<<<<<
        # historial_general.enqueue([nombre_edificio_origen, nombre_edificio_destino, distancia])
        # >>>>>>>>>>>>>>>>>>>>>>>

    def short_viaje(self, viajes):
        min_distancia = 10000000
        for i in range(len(viajes)):
            if viajes[i][2] < min_distancia:
                min_distancia = viajes[i][2]
        return min_distancia

# clase historial. Hereda de cola_nodo    
class Historial(Cola_nodo):
    def __init__(self):
        Cola_nodo.__init__(self)

# se instancia el historial. Solo será uno.
historial_general = Historial()

edificios = [Edificio("Edificio Yu Takeuchi - Departamentos de Matemáticas, Física y Estadística", 404, [4.637574, -74.082677]),
Edificio("Posgrados de Veterinaria", 561, [4.63748670000001, -74.08788838220904]),
Edificio("Postgrados en Bioquímica y Carbones", 452, [4.63711771576264, -74.08447985800483]),
Edificio("Talleres de Mantenimiento", 435, [4.64205482639357, -74.08360455507342]),
Edificio("Departamento de Farmacia", 450, [4.6372861417941635, -74.0834874406681]),
Edificio("Talleres y Aulas de Construcción", 309, [4.6364961955953, -74.08063562901637]),
Edificio("Edificio Antonio Nariño - Departamento de Lingüistica. Departamento de Ingeniería Civil y Agrícola.", 214, [4.633455840055661, -74.084017710065]),
Edificio("Escuela de Artes Plásticas", 301, [4.6363116622260225, -74.08221569333892]),
Edificio("INGEOMINAS", 631, [4.639677206321538, -74.09285172883612]),
Edificio("Aulas de ciencias", 564, [4.6366923269502225, -74.08704273464534]),
Edificio("Edificio Orlando Fals Borda: Departamento de Sociología", 205, [4.634452309547205, -74.08387430410457]),
Edificio("Instituto Pedagógico Arturo Ramírez Montúfar IPARM", 434, [4.641252188515629, -74.08342681259816]),
Edificio("Galpón de Biología", 632, [4.639537853706288, -74.08140592196807]),
Edificio("Facultad de Ciencias Económicas", 310, [4.637211338202991, -74.08076236339367]),
Edificio("Portería Vehicular y Peatonal Calle 53", 901, [4.643509876619225, -74.08327944496652]),
Edificio("Departamento de Biología", 421, [4.640461140973933, -74.08188636841575]),
Edificio("Edificio Rogelio Salmona de Postgrados en Ciencias Humanas", 225, [4.63428460696461, -74.08655977365419]),
Edificio("Instituto de Genética", 426, [4.642876013587281, -74.08300595643392]),
Edificio("Laboratorio de Investigaciones Patológicas", 531, [4.635546811871263, -74.08568235616787]),
Edificio("Aulas de Ingeniería", 453, [4.638454429180191, -74.08373152169051]),
Edificio("Departamento de Química", 451, [4.637764685367428, -74.0835330382217]),
Edificio("Departamento de Lenguas Extranjeras", 229, [4.632726658071325, -74.08451861259083]),
Edificio("Icontec", 910, [4.64384310128761, -74.08342326562031]),
Edificio("Laboratorio de Hidráulica", 409, [4.638559056536617, -74.0817897627584]),
Edificio("Postgrados de Ciencias Económicas", 238, [4.6326404471845875, -74.08322608296592]),
Edificio("Edificio Ciencia y Tecnología - CyT", 454, [4.63805341542632, -74.08471321019677]),
Edificio("Concha Acústica", 761, [4.638552006766316, -74.08720133232909]),
Edificio("Hemeroteca Nacional", 571, [4.636567221308216, -74.09141619550589]),
Edificio("Edificio Uriel Gutiérrez", 861, [4.639765775083737, -74.08997312802975]),
Edificio("Edificio Francisco de Paula Santander: Diseño Gráfico", 217, [4.633585502038007, -74.08328479644659]),
Edificio("Laboratorio de Patología Clínica y Corral de Bovinos", 506, [4.63407663033411, -74.08764236217705]),
Edificio("Laboratorios de Ingeniería", 411, [4.639156512406468, -74.08260117712538]),
Edificio("Instituto Interamericano de Cooperación para la Agricultura", 606, [4.63654690677914, -74.07985432067237]),
Edificio("Museo de Arquitectura Leopoldo Rother", 207, [4.634041664995465, -74.0832540028815]),
Edificio("Departamento de Cine y Televisión", 701, [4.640524964983155, -74.0855220734337]),
Edificio("Conservatorio de Música", 305, [4.635571117486736, -74.08117231672759]),
Edificio("Escuela de Arquitectura", 303, [4.636736734275307, -74.08160415237948]),
Edificio("Parque Automotor", 436, [4.641669240925287, -74.08348313898786]),
Edificio("Portería Peatonal Calle 26", 235, [4.632525465261985, -74.08392775782852]),
Edificio("Centro de Acopio de Residuos Sólidos", 437, [4.641302342792041, -74.08397457887394]),
Edificio("Polideportivo", 103, [4.634831099102443, -74.0829975949591]),
Edificio("Postgrados en Materiales y Procesos de Manufactura", 407, [4.639263646631807, -74.0822111001772]),
Edificio("Filosofía", 239, [4.6323455717377335, -74.08331072877552]),
Edificio("Central Telefónica", 614, [4.639487623871562, -74.08182737609188]),
Edificio("Postgrados en Matemáticas y Física", 405, [4.637758348985364, -74.08172452460337]),
Edificio("Museo de Arte", 317, [4.634562273519589, -74.08083133763094]),
Edificio("Facultad de Enfermería (Nuevo)", 228, [4.635232340842952, -74.08494106051288]),
Edificio("Laboratorios de Ingeniería Química", 412, [4.6389666994381455, -74.083267706068]),
Edificio("Edificio Julio Garavito Armero - Facultad de Ingeniería", 401, [4.637304, -74.082760]),
Edificio("Biblioteca Gabriel García Márquez", 102, [4.635317306785998, -74.0832505028769]),
Edificio("Instituto de Extensión e Investigación - IEI", 406, [4.638256683909461, -74.08243470824875]),
Edificio("Unidad Camilo Torres", 862, [4.6412660788049696, -74.09016087044806]),
Edificio("Centro en Investigación y Desarrollo en Información Geográfica", 610, [4.638975614471228, -74.07985315267682]),
Edificio("Laboratorio de Inseminación y Corral de Equinos", 505, [4.636045221699395, -74.08627110167642]),
Edificio("Facultad de Medicina Veterinaria y Zootecnia", 481, [4.6363770017064345, -74.08538734398451]),
Edificio("Portería Acceso Vehicular Capilla", 252, [4.632485465444149, -74.08164199400272]),
Edificio("Bloque II Facultad de Ciencias Económicas", 311, [4.637604640600882, -74.08095740145617]),
Edificio("Aulas de Ciencias Humanas", 212, [4.634068726652622, -74.08467820403695]),
Edificio("Almacén e Imprenta", 433, [4.641166639263639, -74.08353141874946]),
Edificio("Instituto Geográfico Agustín Codazzi", 621, [4.638453218276424, -74.07992745503311]),
Edificio("Portería Salida Vehicular Capilla", 253, [4.633450579117872, -74.08073540735573]),
Edificio("Facultad de Odontología", 210, [4.634559664993099, -74.08522267343369]),
Edificio("Restaurante 'Campus' de Ciencias Humanas", 213, [4.633767964486836, -74.08430738863912]),
Edificio("Capilla", 251, [4.632884886630808, -74.08151230506716]),
Edificio("Postgrados en Arquitectura - SINDU", 314, [4.635824135627152, -74.08066504067277]),
Edificio("Facultad de Derecho, Ciencias Politicas y Sociales", 201, [4.635419923588457, -74.08383511471597]),
Edificio("Cancha de Voleibol", 496, [4.639264502618763, -74.08594272465304]),
Edificio("Instituto Pedagógico Arturo Ramírez Montúfar: IPARM", 431, [4.6410794814153045, -74.08282490732093]),
Edificio("Edificio Manuel Ancízar", 224, [4.634000553899457, -74.0860850226576]),
Edificio("Estadio de fútbol", 731, [4.640395358900369, -74.08641613454455]),
Edificio("Cafetería de Odontología", 211, [4.63436948868896, -74.08547414956642]),
Edificio("Perrera", 473, [4.63521513758165, -74.08591928063423]),
Edificio("Aula y Laboratorios de Histopatología e Inseminación", 502, [4.635341179044406, -74.08559022802966]),
Edificio("Cirugía y Clínica de Grandes Animales", 501, [4.636374918125814, -74.08628803110601]),
Edificio("Clínica de Pequeños Animales", 507, [4.636532650604323, -74.08631418264409]),
Edificio("Facultad de Ciencias Agrarias", 500, [4.635867885293131, -74.08711510288151]),
Edificio("Laboratorio de Ensayos Hidráulicos", 408, [4.63821149349025, -74.08149173609216]),
Edificio("Instituto de Ciencias Naturales", 425, [4.6422771700375804, -74.0819424605535]),
Edificio("Dirección Nacional de Innovación Académica", 477, [4.636864549649436, -74.08534437211763]),
Edificio("Canchas de Tenis T-2, T-3 y T-4", 414, [4.639525444501469, -74.08367406073157]),
Edificio("Facultad de Ciencias", 476, [4.637287619874028, -74.08552072736123]),
Edificio("Facultad de Medicina", 471, [4.6364119300590705, -74.08442889603137]),
Edificio("León de Greiff", 104, [4.635679915166562, -74.08233173656821]),
Edificio("Torre de Enfermería", 101, [4.635168159913767, -74.08241720288407]),
Edificio("Observatorio Astronómico", 413, [4.639806153566646, -74.08336158338332]),
Edificio("Banco Popular", 230, [4.632901877394506, -74.08477948528329]),
Edificio("Portería Calle 45", 603, [4.639658562129161, -74.0889847886104]),
Edificio("Patología Aviar, Gallinero y Perrera", 504, [4.634075088678774, -74.08764302439064])]

Edificios_Nombre = []
Edificios_Numero = []
Ed_Num = []
Edificios_coordenadas = []

for i in edificios:
    Edificios_coordenadas.append(i.coordenadas[0])

Edificios2 = []
Edificios_coordenadas.sort()



for i in range(len(edificios)):
    for j in range(len(Edificios_coordenadas)):
        if edificios[j].coordenadas[0] == Edificios_coordenadas[i]:
            Edificios2.append(edificios[j])

for i in Edificios2:
    Edificios_Nombre.append(unicodedata.normalize('NFKD', i.nombre_edificio).encode('ASCII', 'ignore').lower())
    Edificios_Numero.append(unicodedata.normalize('NFKD', str(i.num_edificio)).encode('ASCII', 'ignore').lower())
    Ed_Num.append(i.num_edificio)

#inicio1=time()
arbol_edificios = arbol_BST.BST()
for i in range(len(edificios)):
    arbol_edificios.BST_insert(edificios[i])
#fin1=time()-inicio1
#print(fin1)
def distancia_puntos(lat1,lon1,lat2,lon2):
        inicio = (radians(lat1), radians(lon1))
        final = (radians(lat2), radians(lon2))
        distancia = acos(
            sin(inicio[0]) * sin(final[0]) + cos(inicio[0]) * cos(final[0]) * cos(inicio[1] - final[1]))
        return round(distancia * 6371.01 * 1000, 2)  # retorna distancia en metros

Grafosun = Grafos.Graph()
for i in range(len(edificios)):
    Grafosun.add_vertex(edificios[i].num_edificio)

Grafosun.add_edge(edificios[0].num_edificio, edificios[1].num_edificio,distancia_puntos(edificios[0].coordenadas[0],edificios[0].coordenadas[1], edificios[1].coordenadas[0],edificios[1].coordenadas[1]))
Grafosun.add_edge(edificios[0].num_edificio, edificios[2].num_edificio,distancia_puntos(edificios[0].coordenadas[0],edificios[0].coordenadas[1], edificios[2].coordenadas[0],edificios[2].coordenadas[1]))
Grafosun.add_edge(edificios[1].num_edificio, edificios[3].num_edificio,distancia_puntos(edificios[1].coordenadas[0],edificios[1].coordenadas[1], edificios[3].coordenadas[0],edificios[3].coordenadas[1]))
Grafosun.add_edge(edificios[2].num_edificio, edificios[4].num_edificio,distancia_puntos(edificios[2].coordenadas[0],edificios[2].coordenadas[1], edificios[4].coordenadas[0],edificios[4].coordenadas[1]))
Grafosun.add_edge(edificios[3].num_edificio, edificios[5].num_edificio,distancia_puntos(edificios[3].coordenadas[0],edificios[3].coordenadas[1], edificios[5].coordenadas[0],edificios[5].coordenadas[1]))
Grafosun.add_edge(edificios[4].num_edificio, edificios[6].num_edificio,distancia_puntos(edificios[4].coordenadas[0],edificios[4].coordenadas[1], edificios[6].coordenadas[0],edificios[6].coordenadas[1]))
Grafosun.add_edge(edificios[5].num_edificio, edificios[7].num_edificio,distancia_puntos(edificios[5].coordenadas[0],edificios[5].coordenadas[1], edificios[7].coordenadas[0],edificios[7].coordenadas[1]))
Grafosun.add_edge(edificios[6].num_edificio, edificios[8].num_edificio,distancia_puntos(edificios[6].coordenadas[0],edificios[6].coordenadas[1], edificios[8].coordenadas[0],edificios[8].coordenadas[1]))
Grafosun.add_edge(edificios[7].num_edificio, edificios[9].num_edificio,distancia_puntos(edificios[7].coordenadas[0],edificios[7].coordenadas[1], edificios[9].coordenadas[0],edificios[9].coordenadas[1]))
Grafosun.add_edge(edificios[8].num_edificio, edificios[10].num_edificio,distancia_puntos(edificios[8].coordenadas[0],edificios[8].coordenadas[1], edificios[10].coordenadas[0],edificios[10].coordenadas[1]))
Grafosun.add_edge(edificios[9].num_edificio, edificios[11].num_edificio,distancia_puntos(edificios[9].coordenadas[0],edificios[9].coordenadas[1], edificios[11].coordenadas[0],edificios[11].coordenadas[1]))
Grafosun.add_edge(edificios[10].num_edificio, edificios[11].num_edificio,distancia_puntos(edificios[10].coordenadas[0],edificios[10].coordenadas[1], edificios[11].coordenadas[0],edificios[11].coordenadas[1]))

#print(dijkstra_algorithm(Grafosun, Grafosun.get_vertex(404)))

for i in Edificios2:
    print(i.num_edificio)


#path = Grafos.shortest(target, path)
#print(path)
