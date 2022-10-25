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


# Numero de paneles
def calcular_paneles() :

    try:
        consumo = float(caja_consumo_diario.get())
        consumo_individual = float(caja_consumo_individual.get())
        potencia_panel = float(caja_potencia_panel.get())
        eficiencia_inversor = float(caja_eficiencia_del_inversor.get())/100
        capacidad_individual_baterias = float(caja_capacidad_baterias.get())
        dias_de_autonomia = float(caja_días_de_operacion.get())
        corriente_panel = float(caja_corriente_panel.get())
        potencia_unitaria_ac = float(caja_potencia_unitaria_ac.get())
        horas_solares = float(caja_horas_solares.get())
        voltaje_sistema = float(caja_voltaje_sistema.get())
        profundidad_de_descarga = float(caja_profundidad_de_descarga.get())/100
        voltaje_baterias = float(caja_voltaje_baterias.get())
        
    except:
        messagebox.showinfo('Warning','Entrada Inválida. Intente de Nuevo')

    # Cálculo de paneles Aproximado    
    consumo_con_factor_de_error = consumo*(1.2)
    eficiencia_panel = 0.9
    numero_de_paneles = consumo_con_factor_de_error/(horas_solares*eficiencia_panel*potencia_panel)
    etiqueta_numero_de_paneles_aprox.config(text=f"Número de paneles necesarios aproximados: {math.ceil(numero_de_paneles)} módulos")
    
    # Cálculo de paneles Exacto
    eficiencia_bateria = 0.95
    eficiencia_controlador = 1
    numero_de_paneles_2 = (consumo_con_factor_de_error/eficiencia_inversor*eficiencia_controlador*eficiencia_bateria)/(horas_solares*eficiencia_panel*potencia_panel)
    etiqueta_numero_de_paneles_exac.config(text=f"Número de paneles necesarios exactos: {math.ceil(numero_de_paneles_2)} módulos")

    # Cálculo acumuladores
    c_a = consumo_con_factor_de_error*dias_de_autonomia/(voltaje_sistema*profundidad_de_descarga)
    etiqueta_c_a.config(text=f"Cálculo acumuladores: {round(c_a)} Ah")
    
    # Número de Baterías
    arreglo_de_baterias = math.ceil(c_a/capacidad_individual_baterias)
    numero_baterias = arreglo_de_baterias*(voltaje_sistema/voltaje_baterias)
    baterias_por_arreglo = numero_baterias / arreglo_de_baterias
    etiqueta_numero_baterias.config(text=f"Número de baterías: {math.ceil(numero_baterias)} en {arreglo_de_baterias} arreglos de {math.ceil(baterias_por_arreglo)} baterías")

    # Controldor de carga
    corriente_entrada = 1.25*math.ceil(numero_de_paneles_2)*corriente_panel
    etiqueta_corriente_de_entrada.config(text=f"Corriente de entrada del C.C.: {round(corriente_entrada)} A")
    corriente_salida = 1.25*(consumo_individual/eficiencia_inversor)/voltaje_sistema
    etiqueta_corriente_de_salida.config(text=f"Corriente de salida del C.C.: {round(corriente_salida)} A")
    
    # Potencia Inversor
    potencia_inversor = 1.2 * potencia_unitaria_ac
    etiqueta_potencia_inversor.config(text=f"Potencia del inversor: {round(potencia_inversor)} W")

#-----------------------------------------------------------------------------------------------------------
    
ventana = tk.Tk()                                                              # Se crea la ventana
ventana.title("PV calculator")                                                 # Título de la ventana
ventana.resizable(0,0)                                                         # No deja redimensionar 
ventana.config(width=800, height=620)                                          # Dimensiones
ventana.config(bg='white')                                                     # color del fondo



#--------------------------------- Estética ----------------------------------------------

ventana.iconbitmap("Icono1.ico")

#icono_grande = tk.PhotoImage(file="P1.png")

imagen = PhotoImage(file = "P4.png")

# Con Label y la opción image, puedes mostrar una imagen en el widget:
background = Label(image = imagen, text = "Icono.ico")

# Con place puedes organizar el widget de la imagen posicionandolo
# donde lo necesites (relwidth y relheight son alto y ancho en píxeles):
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)



#-----------------------------------------------------------------------------------------------------------------

entry = ttk.Label(text="CALCULADORA DE SISTEMAS FOTOVOLTAICOS")                # Nombre de la etiqueta
entry.place(x=250, y=10)                                                       # Posición de la etiqueta



#-----------------------------------------------------------------------------------------------------------------
#--------------------------------- Pedir la potencia unitaria en AC ----------------------------------------------


etiqueta_potencia_unitaria_ac = ttk.Label(text="Potencia unitaria en AC (W):") # Nombre de la etiqueta
etiqueta_potencia_unitaria_ac.place(x=70, y=70)                                # Posición de la etiqueta     


#--------------------------------- Caja para la potencia unitaria en AC ----------------------------------------------

caja_potencia_unitaria_ac =  ttk.Entry()                                       # Creación de la caja para los valores
caja_potencia_unitaria_ac.place(x=226, y=70, width=50)                         # Posición y ancho de la caja





#-------------------------------------------------------------------------------------------------------------------
#-------------------------------- Pedir consumo diario -------------------------------------------------------------  

entry = ttk.Label(text="Datos consumo")                                        # Nombre de la etiqueta
entry.place(x=70, y=40)                                                        # Posición de la etiqueta

etiqueta_consumo_diario = ttk.Label(text="Consumo Diario en AC (W):")          # Nombre de la etiqueta
etiqueta_consumo_diario.place(x=70, y=96)                                      # Posición de la etiqueta


#--------------------------------- Caja para el valor de consumo----------------------------------------------

caja_consumo_diario = ttk.Entry()                                              # Creación de la caja para los valores
caja_consumo_diario.place(x=222, y=95, width=50)                               # Posición y ancho de la caja






#----------------------------------------------------------------------------------------------------------------
#-------------------------------- Pedir consumo individual ------------------------------------------------------

etiqueta_consumo_individual = ttk.Label(text="Consumo Individual en AC (W):")  # Nombre de la etiqueta
etiqueta_consumo_individual.place(x=70, y=121)                                 # Posición de la etiqueta


#--------------------------------- Caja para consumo individual----------------------------------------------

caja_consumo_individual = ttk.Entry()                                          # Creación de la caja para los valores
caja_consumo_individual.place(x=243, y=120, width=50)                          # Posición y ancho de la caja




#----------------------------------------------------------------------------------------------------------------
#-------------------------------- Pedir Horas solares pico ------------------------------------------------------

etiqueta_horas_solares = ttk.Label(text="Horas solares pico (h):")             # Nombre de la etiqueta
etiqueta_horas_solares.place(x=70, y=146)                                      # Posición de la etiqueta


#--------------------------------- Caja para Horas solares pico ----------------------------------------------

caja_horas_solares = ttk.Entry()                                               # Creación de la caja para los valores
caja_horas_solares.place(x=192, y=145, width=50)                               # Posición y ancho de la caja





#--------------------------------------------------------------------------------------------------------------------

entry = ttk.Label(text="Datos panel")                                          # Nombre de la etiqueta
entry.place(x=70, y=194)                                                       # Posición de la etiqueta




#----------------------------------------------------------------------------------------------------------------
#-------------------------------- Pedir potencia del panel-------------------------------------------------------

etiqueta_potencia_panel = ttk.Label(text="Potencia del Panel(W):")             # Nombre de la etiqueta
etiqueta_potencia_panel.place(x=70, y=218)                                     # Posición de la etiqueta


#--------------------------------- Caja para el valor de potencia panel----------------------------------------------

caja_potencia_panel = ttk.Entry()                                              # Creación de la caja para los valores
caja_potencia_panel.place(x=195, y=217, width=50)                              # Posición y ancho de la caja





#---------------------------------------------------------------------------------------------------------------------
#-------------------------------- Pedir corriente del panel-----------------------------------------------

etiqueta_corriente_panel = ttk.Label(text="Corriente del Panel(A):")           # Nombre de la etiqueta
etiqueta_corriente_panel.place(x=70, y=243)                                    # Posición y ancho de la etiqueta


#--------------------------------- Caja para el valor de corriente panel----------------------------------------------

caja_corriente_panel = ttk.Entry()                                             # Creación de la caja para los valores
caja_corriente_panel.place(x=195, y=242, width=50)                             # Posición y ancho de la caja




#----------------------------------------------------------------------------------------------------------------
entry = ttk.Label(text="Datos baterías")                                       # Nombre de la etiqueta
entry.place(x=70, y=292)                                                       # Posición de la etiqueta



#--------------------------------- Pedir voltaje de baterias ----------------------------------------------


etiqueta_voltaje_baterias = ttk.Label(text="Voltaje Baterías(V):")             # Nombre de la etiqueta
etiqueta_voltaje_baterias.place(x=70, y=317)                                   # Posición de la etiqueta

#--------------------------------- Caja para voltaje de baterias ----------------------------------------------

caja_voltaje_baterias = ttk.Combobox(values=["2", "6", "12", "24", "48"], state="readonly")    # Creación de la caja con los valores
caja_voltaje_baterias.place(x=174, y=316, width=50)                                            # Posición y ancho de la caja





#--------------------------------------------------------------------------------------------------------------------
#--------------------------------- Pedir corriente de baterias ----------------------------------------------

etiqueta_capacidad_baterias = ttk.Label(text="Capacidad Baterías(Ah):")        # Nombre de la etiqueta
etiqueta_capacidad_baterias.place(x=70, y=342)                                 # Posición de la etiqueta


#--------------------------------- Caja para corriente de baterias ----------------------------------------------

caja_capacidad_baterias = ttk.Entry()                                          # Creación de la caja para los valores
caja_capacidad_baterias.place(x=202, y=341, width=50)                          # Posición y ancho de la caja




#--------------------------------------------------------------------------------------------------------------------
#--------------------------------- Pedir profundidad de descarga ----------------------------------------------

etiqueta_profundidad_de_descarga = ttk.Label(text="Profundidad de descarga de las baterias(%):")      # Nombre de la etiqueta
etiqueta_profundidad_de_descarga.place(x=70, y=367)                                                   # Posición de la etiqueta


#--------------------------------- Caja para profundidad de descarga ----------------------------------------------

caja_profundidad_de_descarga = ttk.Combobox(values=["60", "80", "85", "90", "95"], state="readonly")  # Creación de la caja con los valores
caja_profundidad_de_descarga.place(x=306, y=366, width=50)                                            # Posición y ancho de la caja




#-------------------------------------------------------------------------------------------------------------------

entry = ttk.Label(text="Datos inversor")                                       # Nombre de la etiqueta
entry.place(x=70, y=416)                                                       # Posición de la etiqueta 





#--------------------------------------------------------------------------------------------------------------------
#-------------------------------- Pedir factor de seguridad del inversor -----------------------------------------------

etiqueta_factor_inversor = ttk.Label(text="Factor del inversor(%):")           # Nombre de la etiqueta
etiqueta_factor_inversor.place(x=70, y=440)                                    # Posición de la etiqueta     


#--------------------------------- Caja para el factor de seguridad del inversor ----------------------------------------------

caja_factor_inversor = ttk.Combobox(values=["0", "20", "25", "30", "50"], state="readonly")  # Creación de la caja con los valores
caja_factor_inversor.place(x=194, y=439, width=50)                                           # Posición y ancho de la caja





#--------------------------------------------------------------------------------------------------------------------
#-------------------------------- Pedir eficiencia del inversor -----------------------------------------------

etiqueta_eficiencia_del_inversor = ttk.Label(text="Eficiencia del Inversor(%): ")     # Nombre de la etiqueta
etiqueta_eficiencia_del_inversor.place(x=70, y=464)                                   # Posición de la etiqueta


#--------------------------------- Caja para eficiencia del inversor ----------------------------------------------

caja_eficiencia_del_inversor = ttk.Combobox(values=["60", "80", "85", "90", "95"], state="readonly")  # Creación de la caja con los valores
caja_eficiencia_del_inversor.place(x=214, y=463, width=50)                                            # Posición y ancho de la caja





#--------------------------------------------------------------------------------------------------------------------
#-------------------------------- Pedir voltaje del inversor -----------------------------------------------


etiqueta_voltaje_inversor = ttk.Label(text="Voltaje inversor(V):")             # Nombre de la etiqueta
etiqueta_voltaje_inversor.place(x=70, y=489)                                   # Posición de la etiqueta


#--------------------------------- Caja para el voltaje del inversor ----------------------------------------------

caja_voltaje_inversor = ttk.Combobox(values=["12", "24", "48", "96", "120"], state="readonly")  # Creación de la caja con los valores
caja_voltaje_inversor.place(x=175, y=488, width=50)                                             # Posición y ancho de la caja





#--------------------------------------------------------------------------------------------------------------------

entry = ttk.Label(text="Otros datos")                                          # Nombre de la etiqueta
entry.place(x=70, y=540)                                                       # Posición de la etiqueta



#--------------------------------------------------------------------------------------------------------------------
#--------------------------------- Pedir voltaje del sistema ----------------------------------------------

etiqueta_voltaje_sistema = ttk.Label(text="Voltaje Sistema(V):")               # Nombre de la etiqueta
etiqueta_voltaje_sistema.place(x=70, y=566)                                    # Posición de la etiqueta



#--------------------------------- Caja para voltaje del sistema ----------------------------------------------

caja_voltaje_sistema = ttk.Combobox(values=["2", "6", "12", "24", "48"], state="readonly")   # Creación de la caja con los valores
caja_voltaje_sistema.place(x=174, y=565, width=50)                                           # Posición y ancho de la caja





#--------------------------------------------------------------------------------------------------------------------
#--------------------------------- Días de Operación ----------------------------------------------

etiqueta_días_de_operacion = ttk.Label(text="Días de Operación:")              # Nombre de la etiqueta
etiqueta_días_de_operacion.place(x=70, y=591)                                  # Posición de la etiqueta

#--------------------------------- Caja para Días de Operación ----------------------------------------------

caja_días_de_operacion = ttk.Entry()                                           # Creación de la caja para los valores
caja_días_de_operacion.place(x=175, y=590, width=50)                           # Posición y ancho de la caja





#---------------------------------------------------------------------------------------------------------------

#--------------------------------------- llamar las funciones---------------------------------------------------
#                                          
boton_calcular_paneles = ttk.Button(text="Calcular", command = calcular_paneles)
boton_calcular_paneles.place(x=480, y=60)

etiqueta_numero_de_paneles_aprox = ttk.Label(text='Número de paneles necesarios aprox: n/a')
etiqueta_numero_de_paneles_aprox.place(x=480, y=100)

etiqueta_numero_de_paneles_exac = ttk.Label(text='Número de paneles necesarios exac: n/a')
etiqueta_numero_de_paneles_exac.place(x=480, y=130)

etiqueta_c_a = ttk.Label(text='Cálculo acumuladores: n/a')
etiqueta_c_a.place(x=480, y=160)

etiqueta_numero_baterias = ttk.Label(text='Número baterías: n/a')
etiqueta_numero_baterias.place(x=480, y=190)

etiqueta_corriente_de_entrada = ttk.Label(text='Corriente de entrada del C.C: n/a')
etiqueta_corriente_de_entrada.place(x=480, y=220)

etiqueta_corriente_de_salida = ttk.Label(text='Corriente de salida del C.C: n/a')
etiqueta_corriente_de_salida.place(x=480, y=250)

etiqueta_potencia_inversor = ttk.Label(text='Potencia del inversor: n/a')
etiqueta_potencia_inversor.place(x=480, y=280)


ventana.mainloop()                                                             # Se cierra el bucle
