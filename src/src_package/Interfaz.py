from tkinter import *
import time
from tkinter.ttk import Notebook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkintermapview

raiz = Tk()
raiz.title("MovilizateUN")
raiz.resizable(False,False)
raiz.geometry("360x640")

notebook=Notebook(raiz)
notebook.grid()

#para cuadros de texto
arriba=Frame()
arriba.config(width="360", height="65", bg="#466b3f")
arriba.place(x=0, y=0)

#para el mapa
centro=Frame()
centro.config(width="360", height="510",bg="white")
centro.place(x=0, y=65)

#para los botones
abajo=Frame()
abajo.config(width="360",height="65", bg="#466b3f")
abajo.place(x=0, y=575)

#Texto en el centro
welcome=Label(centro, text="¡Bienvenidx! Ingresa tu edificio de origen\ny de destino para iniciar el viaje", font="Candara, 20",bg='white', fg="black")
welcome.place(x=0, y=220)

#crear el mapa
map_widget = tkintermapview.TkinterMapView(raiz, width=250, height=350, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

#coordenadas del mapa
map_widget.set_position(4.638116020576138, -74.08406346406575)
map_widget.set_zoom(15)

#crear marcadores
marcador_origen = map_widget.set_marker(0,0)
marcador_destino = map_widget.set_marker(0,0)

#Entradas
origen=StringVar()
destino=StringVar()

#Entradas de destino y origen
origin=Label(arriba,text="Desde:", font="Candara, 13",fg="white", bg="#466b3f")
origin.place(x=25, y=4)
entrada1=Entry(arriba,textvariable=origen)
entrada1.place(x=100,y=4)
destiny=Label(arriba,text="Hasta:", font="Candara 13", fg="white", bg="#466b3f")
destiny.place(x=25, y=35)
entrada2=Entry(arriba, textvariable=destino)
entrada2.place(x=100, y=35)

#Extrae info y la retorna
def crearViaje():
    desde=origen.get()
    hasta=destino.get()
    
    #posicion y texto de los marcadores
    marcador_origen.set_position(4.637574, -74.082677) 
    marcador_origen.set_text(desde)
    marcador_destino.set_position(4.638007, -74.084678)
    marcador_destino.set_text(hasta)
    
    return desde,hasta

#Eliminar marcadores
def finalizarViaje():
    marcador_origen.set_position(0,0)
    marcador_destino.set_position(0,0)

#logo
foto_logo =PhotoImage(file="logo1.gif")
logo=Label(arriba, image=foto_logo, bg="#466b3f")
logo.place(x=300, y=4)

#iniciar viaje
inViaje=Button(abajo, text="Iniciar Viaje", command=crearViaje, bg="#466b3f", fg="black")
inViaje.place(x=20, y=15)

#Finalizar viaje
finViaje=Button(abajo, text="Finalizar Viaje", command = finalizarViaje, bg="#466b3f", fg="black")
finViaje.place(x=100, y=15)

def abrirHist():
    welcome.destroy()
    inViaje.destroy()
    finViaje.destroy()
    historial.destroy()
    volver.place(x=20, y=15)
    #añade los viajes y los muestra en pantalla

#boton historial
historial=Button(abajo, text="Historial", command=abrirHist, bg="#466b3f", fg="black")
historial.place(x=230, y=15)

def devolver():
    #borra el historial
    inViaje.place(x=20, y=15)
    finViaje.place(x=100, y=500)
    historial.place(x=230, y=15)

#boton volver
volver=Button(abajo, text="Volver", command="devolver", bg="#466b3f", fg="black")

raiz.mainloop()
