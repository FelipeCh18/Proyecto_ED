from tkinter import *
from tkinter import messagebox
import time
from tkinter.ttk import Notebook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkintermapview
import unicodedata
from prototipo import *
from prototipo import edificios as info_ubicacion, Edificios_Nombre as info_nombre, Edificios_Numero as info_num

raiz = Tk()
raiz.title("MovilizateUN")
raiz.resizable(False, False)
raiz.geometry("360x640")

notebook = Notebook(raiz)
notebook.grid()

# para cuadros de texto
arriba = Frame()
arriba.config(width="360", height="65", bg="#466b3f")
arriba.place(x=0, y=0)

# para el mapa
centro = Frame()
centro.config(width="360", height="510", bg="white")
centro.place(x=0, y=65)

# para los botones
abajo = Frame()
abajo.config(width="360", height="65", bg="#466b3f")
abajo.place(x=0, y=575)

# Texto en el centro
welcome = Label(centro, text="¡Bienvenidx! Ingresa tu edificio de origen\ny de destino para iniciar el viaje",
                font="Candara, 20", bg='white', fg="black")
welcome.place(x=0, y=220)

# crear el mapa
map_widget = tkintermapview.TkinterMapView(raiz, width=250, height=350, corner_radius=0)

# coordenadas del mapa
map_widget.set_position(4.638116020576138, -74.08406346406575)
map_widget.set_zoom(15)

# crear marcadores
marcador_origen = map_widget.set_marker(0, 0)
marcador_destino = map_widget.set_marker(0, 0)

# Entradas
origen = StringVar()
destino = StringVar()

# Entradas de destino y origen
origin = Label(arriba, text="Desde:", font="Candara, 13", fg="white", bg="#466b3f")
origin.place(x=25, y=4)
entrada1 = Entry(arriba, textvariable=origen)
entrada1.place(x=100, y=4)
destiny = Label(arriba, text="Hasta:", font="Candara 13", fg="white", bg="#466b3f")
destiny.place(x=25, y=35)
entrada2 = Entry(arriba, textvariable=destino)
entrada2.place(x=100, y=35)


# Extrae info y la retorna
def crearViaje():
    map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)
    welcome.destroy()

    desde = origen.get()
    hasta = destino.get()

    desde = origen.get()
    desde = unicodedata.normalize('NFKD', str(desde)).encode('ASCII', 'ignore').lower()
    hasta = destino.get()
    hasta = unicodedata.normalize('NFKD', str(hasta)).encode('ASCII', 'ignore').lower()
    # comprobar si los datos ingresados existen
    if (desde in info_nombre and hasta in info_nombre) or (desde in info_num and hasta in info_num):

        desde_ubicacion = info_ubicacion[info_nombre.index(desde)]

        marcador_origen.set_position(desde_ubicacion.coordenadas[0], desde_ubicacion.coordenadas[1])
        marcador_origen.set_text(desde.upper())

        hasta_ubicacion = info_ubicacion[info_nombre.index(hasta)]
        marcador_destino.set_position(hasta_ubicacion.coordenadas[0], hasta_ubicacion.coordenadas[1])
        marcador_destino.set_text(hasta.upper())

        # buscar la informacion en el arbol BST
        ori = arbol_edificios.find(desde_ubicacion.num_edificio, arbol_edificios.root)
        dest = arbol_edificios.find(hasta_ubicacion.num_edificio, arbol_edificios.root)

        # calcular distancia entre puntos
        viaje1 = Viaje(ori, dest)
        viaje1.hacer_viaje()
        historial_general.print_list()

        # mostrar la distancia en pantalla
        # distancia = Label(text = str(viaje1.hacer_viaje()), font="Candara, 20",bg='white', fg="black")
        # distancia.place(x=100, y=220)
    else:
        print(messagebox.showinfo(message='Ingrese un edificio valido', title='Edificio no encontrado'))

    return desde, hasta


# Eliminar marcadores
def finalizarViaje():
    marcador_origen.set_position(0, 0)
    marcador_destino.set_position(0, 0)


# logo
foto_logo = PhotoImage(file="logo1.gif")
logo = Label(arriba, image=foto_logo, bg="#466b3f")
logo.place(x=300, y=4)

# iniciar viaje
inViaje = Button(abajo, text="Iniciar Viaje", command=crearViaje, bg="#466b3f", fg="black")
inViaje.place(x=20, y=15)

# Finalizar viaje
finViaje = Button(abajo, text="Finalizar Viaje", command=finalizarViaje, bg="#466b3f", fg="black")
finViaje.place(x=100, y=15)


def abrirHist():
    global tam_barra, expanded
    # abrir la barra lateral
    if expanded is False:
        tam_barra += 10
        rep = raiz.after(5, abrirHist)
        barra.config(width=tam_barra)
        if tam_barra >= max_barra:
            expanded = True
            raiz.after_cancel(rep)
            fill()
    # cerrar la barra lateral
    else:
        tam_barra -= 10
        rep = raiz.after(5, abrirHist)
        barra.config(width=tam_barra)
        if tam_barra <= min_barra:
            expanded = False
            raiz.after_cancel(rep)
            fill()
    # añade los viajes y los muestra en pantalla


# comprobar si la barra esta abierta
def fill():
    if expanded:
        texto_viajes.config(text='Últimos viajes', image='', font=(0, 21))
    else:
        texto_viajes.config(text="")


# boton historial
historial = Button(abajo, text="Historial", command=abrirHist, bg="#466b3f", fg="black")
historial.place(x=230, y=15)

# propiedades de la barra lateral
min_barra = 10
max_barra = 200
tam_barra = 10
expanded = False

# crear la barra lateral para el historial
raiz.update()
barra = Frame(raiz, bg="#466b3f", width=10, height=raiz.winfo_height())
barra.grid(row=0, column=0)
texto_viajes = Label(barra, bg="white", font="Candara 13", relief='flat')
texto_viajes.grid(row=0, column=0, pady=10)
barra.grid_propagate(False)

# boton volver
volver = Button(abajo, text="Volver", command="devolver", bg="#466b3f", fg="black")

raiz.mainloop()