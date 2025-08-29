#impotacion de librerias
import tkinter as tk
from tkinter import ttk,messagebox
#crear vetnana principal
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Libro de Pacientes y Doctores")
ventanaPrincipal.geometry("400x600")
#crear contenedor Notebook(Pestaña)
pestañas=ttk.Notebook(ventanaPrincipal)
#crear frames(uno por pestaña)
framePacientes=ttk.Frame(pestañas)
#agregar pestañas al Notebook
pestañas.add(framePacientes,text="Pacientes")
#mostrar las pestañas en la ventana
pestañas.pack(expand=True,fill="both")
#nombre
labelNombre=tk.Label(framePacientes,text="Nombre Completo: ")
labelNombre.grid(row=0, column=0, sticky="w", pady=5,padx=5)
nombreP=tk.Entry(framePacientes)
nombreP.grid(row=0,column=1,sticky="w", pady=5, padx=5)
#fecha de nacimineto
labelFechaN=tk.Label(framePacientes,text="Fecha de Nacimiento:")
labelFechaN.grid(row=1,column=0,sticky="w",pady=5,padx=5)
fechaN=tk.Entry(framePacientes)
fechaN.grid(row=1,column=1,sticky="w",pady=5,padx=5)
#nonbre
labelEdad=tk.Label(framePacientes,text="Edad:")
labelEdad.grid(row=2,column=0,sticky="w",pady=5,padx=5)
edadP=tk.Entry(framePacientes,state="readonly")
edadP.grid(row=2, column=1,sticky="w",pady=5,padx=5)
 
#crear frames doctores
frameDoctores=ttk.Frame(pestañas)
pestañas.add(frameDoctores,text="Doctores")
pestañas.pack(expand=True,fill="both")
 
 
 
#GENERO
labelGenero=tk.Label(framePacientes, text="Género:")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("Masculino")
radioMasculino=ttk.Radiobutton(framePacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(framePacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=3, column=2, sticky="w", padx=5)
 
#GRUPO SANGUINEO
labelGrupoSanguineo=tk.Label(framePacientes, text="Grupo Sanguíneo:")
labelGrupoSanguineo.grid(row=4, column=0, sticky="w", padx=5, pady=5)
GrupoSanguineoEntry=tk.Entry(framePacientes)
GrupoSanguineoEntry.grid(row=4, column=1, sticky="w", pady=5, padx=5)
 
#TIPO DE SEGURO
labelTipoSeguro=tk.Label(framePacientes, text="Tipo de Seguro:")
labelTipoSeguro.grid(row=5, column=0, sticky="w", padx=5, pady=5)
tipoSeguro=tk.StringVar()
tipoSeguro.set("Público")
comboTipoSeguro=ttk.Combobox(framePacientes, values=["Público", "Privado", "Ninguno"], textvariable=tipoSeguro)
comboTipoSeguro.grid(row=5, column=1, sticky="w", pady=5, padx=5)
 
#CENTRO MEDICO
labelCentroMedico=tk.Label(framePacientes, text="Centro de Salud:")
labelCentroMedico.grid(row=6, column=0, sticky="w", padx=5, pady=5)
centroMedico=tk.StringVar()
centroMedico.set("Hospital Central")
comboCentroMedico=ttk.Combobox(framePacientes, values=["Hospital Central", "Clínica Norte", "Centro Sur"], textvariable=centroMedico)
comboCentroMedico.grid(row=6, column=1, sticky="w", pady=5, padx=5)

ventanaPrincipal.mainloop()
























