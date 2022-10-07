# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:15:23 2022

@author: JESID PEREZ; @author: JESUS SANTANA; @author: JUAN MONSALVE
"""
import math # math.ceil # pasa al valor siguiente 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#def convertir_temp():
#    temp_celsius = float(caja_temp_celsius.get())
#    temp_kelvin = temp_celsius + 273.15
#    temp_fahrenheit = temp_celsius*1.8 + 32
#    etiqueta_temp_kelvin.config(text=f"Temperatura en K: {temp_kelvin}")
#    etiqueta_temp_fahrenheit.config(text=f"Temperatura en ºF: {temp_fahrenheit}")

# Numero de paneles
def calcular_paneles() :
    # Aproximado    
    try:
        consumo = float(caja_consumo_diario.get())
        potencia_panel = float(caja_potencia_panel.get())
    except:
        messagebox.showinfo('Warning','Entrada Inválida. Intente de Nuevo')    

    consumo_con_factor_de_error = consumo*(1.2)
    eficiencia_panel = 0.9
    horas_solares = 4
    numero_de_paneles = consumo_con_factor_de_error/(horas_solares*eficiencia_panel*potencia_panel)
    etiqueta_numero_de_paneles_aprox.config(text=f"Número de paneles necesarios aproximados: {math.ceil(numero_de_paneles)}")
    
    # Exacto
    eficiencia_bateria = 0.95
    eficiencia_controlador = 1
    eficiencia_inversor = 0.9
    numero_de_paneles_2 = (consumo_con_factor_de_error/eficiencia_inversor*eficiencia_controlador*eficiencia_bateria)/(horas_solares*eficiencia_panel*potencia_panel)
    etiqueta_numero_de_paneles_exac.config(text=f"Número de paneles necesarios exactos: {math.ceil(numero_de_paneles_2)}")
    
#-------------------------------------------------------------------------------
    
ventana = tk.Tk()                                                              # Se crea la ventana
ventana.title("PV calculator")                                                 # Título de la ventana
ventana.resizable(0,0)                                                         # No deja redimensionar 
ventana.config(width=800, height=600)                                          # Dimensiones
ventana.config(bg='white')                                                     # color del fondo

#--------------------------------- Estetica ----------------------------------------------

ventana.iconbitmap("C:/Users/elect/Dropbox/PC/Desktop/Vainas/UPB/\
Semestre 6 - 20222/FotoVoltaico/App/APP-PV-/Aestethic/Icono1.ico")

icono_grande = tk.PhotoImage(file="C:/Users/elect/Dropbox/PC/Desktop/Vainas/UPB/\
Semestre 6 - 20222/FotoVoltaico/App/APP-PV-/Aestethic/Barra.png")

imagen = PhotoImage(file = "C:/Users/elect/Dropbox/PC/Desktop/Vainas/UPB/\
Semestre 6 - 20222/FotoVoltaico/App/APP-PV-/Aestethic/ejemplo1.png")

# Con Label y la opción image, puedes mostrar una imagen en el widget:
background = Label(image = imagen, text = "Imagen")

# Con place puedes organizar el widget de la imagen posicionandolo
# donde lo necesites (relwidth y relheight son alto y ancho en píxeles):
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)


#-------------------------------- Pedir consumo diario -----------------------------------------------

etiqueta_consumo_diario = ttk.Label(text="Consumo diario (Watts):")            # Nombre de la etiqueta
etiqueta_consumo_diario.place(x=10, y=10)                                      # Posición de la etiqueta


#--------------------------------- Caja para el valor de consumo----------------------------------------------

caja_consumo_diario = ttk.Entry()
caja_consumo_diario.place(x=140, y=10, width=50)


#-------------------------------- Pedir potencia del panel-----------------------------------------------

etiqueta_potencia_panel = ttk.Label(text="Potencia del panel(W):")             # Nombre de la etiqueta
etiqueta_potencia_panel.place(x=200, y=10)                                     # Posición de la etiqueta

#--------------------------------- Caja para el valor de potencia panel----------------------------------------------

caja_potencia_panel = ttk.Entry()
caja_potencia_panel.place(x=320, y=10, width=50)


#-------------------------------- Pedir corriente del panel-----------------------------------------------

etiqueta_corriente_panel = ttk.Label(text="Corriente del panel(A):")           # Nombre de la etiqueta
etiqueta_corriente_panel.place(x=200, y=40)                                    # Posición de la etiqueta

#--------------------------------- Caja para el valor de corriente panel----------------------------------------------

caja_corriente_panel = ttk.Entry()
caja_corriente_panel.place(x=320, y=40, width=50)


#--------------------------------- Pedir voltaje de baterias ----------------------------------------------

etiqueta_voltaje_baterias = ttk.Label(text="Voltaje baterias(V):")             # Nombre de la etiqueta
etiqueta_voltaje_baterias.place(x=380, y=10)                                   # Posición de la etiqueta

#--------------------------------- Caja para el valor de baterias ----------------------------------------------


caja_voltaje_baterias = ttk.Combobox(values=["2", "6", "12", "24", "48"], state="readonly")
caja_voltaje_baterias.place(x=480, y=10, width=50)


#-------------------------------- Pedir voltaje del inversor -----------------------------------------------

etiqueta_voltaje_inversor = ttk.Label(text="Voltaje inversor(V):")             # Nombre de la etiqueta
etiqueta_voltaje_inversor.place(x=200, y=70)                                   # Posición de la etiqueta


#--------------------------------- Caja para el voltaje del inversor ----------------------------------------------

caja_voltaje_inversor = ttk.Combobox(values=["12", "24", "48", "96", "120"], state="readonly")
caja_voltaje_inversor.place(x=300, y=70, width=50)



#-------------------------------- Pedir factor de seguridad del inversor -----------------------------------------------

etiqueta_factor_inversor = ttk.Label(text="Factor del inversor(%):")           # Nombre de la etiqueta
etiqueta_factor_inversor.place(x=200, y=100)                                   # Posición de la etiqueta     


#--------------------------------- Caja para el factor de seguridad del inversor ----------------------------------------------

caja_factor_inversor = ttk.Combobox(values=["0", "20", "25", "30", "50"], state="readonly")
caja_factor_inversor.place(x=320, y=100, width=50)





#-----------------------------------------------------------------------------------------------------

#--------------------------------------- llamar las funciones-----------------------------------


#boton_convertir = ttk.Button(text="Convertir", command=convertir_temp)
#boton_convertir.place(x=20, y=60)

                                                 
#etiqueta_temp_kelvin = ttk.Label(text="Temperatura en K: n/a")
#etiqueta_temp_kelvin.place(x=20, y=120)


#etiqueta_temp_fahrenheit = ttk.Label(text="Temperatura en ºF: n/a")
#etiqueta_temp_fahrenheit.place(x=20, y=160)

boton_calcular_paneles = ttk.Button(text="Calcular número de paneles", command = calcular_paneles)
boton_calcular_paneles.place(x=20, y=130)

etiqueta_numero_de_paneles_aprox = ttk.Label(text='Número de paneles necesarios aprox: n/a')
etiqueta_numero_de_paneles_aprox.place(x=20, y=160)

etiqueta_numero_de_paneles_exac = ttk.Label(text='Número de paneles necesarios exac: n/a')
etiqueta_numero_de_paneles_exac.place(x=20, y=180)

ventana.mainloop()
