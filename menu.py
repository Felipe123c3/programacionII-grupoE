import tkinter as tk

from tkinter import messagebox

#Funcion para pacientes

def nuevoPaciente():

ventanaRegistro=tk.Toplevel(ventanaPrincipal)

ventanaRegistro.title("Registro de Paciente")

ventanaRegistro.geometry("400x400")

ventanaRegistro.configure(bg="lightblue")

#nombre

nombreLabel=tk.Label(ventanaRegistro,text="Nombre:",bg="lightblue")

nombreLabel.grid(row=0,column=0,padx=10,pady=5,sticky="n")

entryNombre=tk.Entry(ventanaRegistro)

entryNombre.grid(row=0,column=1,padx=10,pady=5,sticky="we")

#Direccion

direccionLabel=tk.Label(ventanaRegistro,text="Direccion:",bg="lightblue")

direccionLabel.grid(row=1,column=0,padx=10,pady=5,sticky="n")

entryDireccion=tk.Entry(ventanaRegistro)

entryDireccion.grid(row=1, column=1,padx=10,pady=5,sticky="we")

#Telefono

telefonoLabel=tk.Label(ventanaRegistro,text="Telefono:",bg="lightblue")

telefonoLabel.grid(row=2,column=0,padx=10,pady=5,sticky="n")

entryTelefono=tk.Entry(ventanaRegistro)

entryTelefono.grid(row=2,column=1,padx=10,pady=5,sticky="we")

#sexo (radiobutton)

sexoLabel=tk.Label(ventanaRegistro,text="Sexo:",bg="lightblue")

sexoLabel.grid(row=3,column=0,padx=10,pady=5,sticky="n")

sexo=tk.StringVar="Masculino"

rbMasculino=tk.Radiobutton(ventanaRegistro,text="Masculino",variable=sexo,value="Masculino")

rbMasculino.grid(row=3,column=1,sticky="n")

rbFemenino=tk.Radiobutton(ventanaRegistro,text="Femenino",variable=sexo, value="Femenino")

rbFemenino.grid(row=4,column=1,sticky="n")

#enfermedades base(checkbutton)

enfLabel=tk.Label(ventanaRegistro,text="Enfermedades base:",bg="lightblue")

enfLabel.grid(row=5,column=0,padx=10,pady=5,sticky="n")

diabetes=tk.BooleanVar()

hipertension=tk.BooleanVar()

asma=tk.BooleanVar()

cbDiabetes=tk.Checkbutton(ventanaRegistro,text="Diabetes",variable=diabetes)

cbDiabetes.grid(row=5,column=1,sticky="n")

cbHipertension=tk.Checkbutton(ventanaRegistro,text="Hipertension",variable=hipertension)

cbHipertension.grid(row=6,column=1,sticky="n")

cbAsma=tk.Checkbutton(ventanaRegistro,text="Asma",variable=asma)

cbAsma.grid(row=7,column=1,sticky="n")

#Acción: registrar datos

def registrarDatos():

enfermedades=[]

if diabetes.get():

enfermedades.append("Diabetes")

if hipertension.get():

enfermedades.append("Hipertensión")

if asma.get():

enfermedades.append("Asma")

if len(enfermedades)>0:

enfermedadesTexto=','.join(enfermedades)

else:

enfermedadesTexto='Ninguna'

#cadene para mostrar todos los datos del formulario

info=(

f"Nombre:{entryNombre.get()}\n"

f"Dirección:{entryDireccion.get()}\n"

f"Teléfono:{entryTelefono.get()}\n"

f"Sexo:{sexo.get()}\n"

f"Enfermedades:{enfermedadesTexto}"

)

#a la altura de info colocar

messagebox.showinfo("Datos Registrados",info)

ventanaRegistro.destroy() #Cierra la ventana tras el mensaje

#Fuera del def registrarDatos()

btnRegsitrar=tk.Button(ventanaRegistro,text="Datos Registrados",command=registrarDatos)

btnRegsitrar.grid(row=9,column=0,columnspan=2,pady=15)

def buscarPaciente():

messagebox.showinfo("Buscar Paciente","Espacio para buscar pacientes")

def eliminarPaciente():

messagebox.showinfo("Eliminar Paciente","Espacio para eliminar pacientes")

#Funcion para doctores

def nuevoDoctor():

ventanaRegDoc=tk.Toplevel(ventanaPrincipal)

ventanaRegDoc.title("Registro de Doctores")

ventanaRegDoc.geometry("400x400")

ventanaRegDoc.configure(bg="blue")

#nombre

nombreLabel=tk.Label(ventanaRegDoc,text="Nombre:",bg="blue")

nombreLabel.grid(row=0,column=0,padx=10,pady=5,sticky="n")

entryNombre=tk.Entry(ventanaRegDoc)

entryNombre.grid(row=0,column=1,padx=10,pady=5,sticky="we")

#Direccion

direccionLabel=tk.Label(ventanaRegDoc,text="Direccion:",bg="blue")

direccionLabel.grid(row=1,column=0,padx=10,pady=5,sticky="n")

entryDireccion=tk.Entry(ventanaRegDoc)

entryDireccion.grid(row=1, column=1,padx=10,pady=5,sticky="we")

#Telefono

telefonoLabel=tk.Label(ventanaRegDoc,text="Telefono:",bg="blue")

telefonoLabel.grid(row=2,column=0,padx=10,pady=5,sticky="n")

entryTelefono=tk.Entry(ventanaRegDoc)

entryTelefono.grid(row=2,column=1,padx=10,pady=5,sticky="we")

#sexo (radiobutton)

sexoLabel=tk.Label(ventanaRegDoc,text="Sexo:",bg="blue")

sexoLabel.grid(row=3,column=0,padx=10,pady=5,sticky="n")

sexo=tk.StringVar="Masculino"

rbMasculino=tk.Radiobutton(ventanaRegDoc,text="Masculino",variable=sexo,value="Masculino")

rbMasculino.grid(row=3,column=1,sticky="n")

rbFemenino=tk.Radiobutton(ventanaRegDoc,text="Femenino",variable=sexo,value="Femenino")

rbFemenino.grid(row=4,column=1,sticky="n")

#Especialidad











espLabel=tk.Label(ventanaRegDoc,text="especialidad:",bg="lightblue")

espLabel.grid(row=6,column=0,padx=10,pady=5,sticky="n")

cardiologia=tk.BooleanVar()

pediatria=tk.BooleanVar()

oftalmologia=tk.BooleanVar()

cbcardiologia=tk.Checkbutton(ventanaRegDoc,text="cardiologia",variable=cardiologia)

cbcardiologia.grid(row=7,column=1,sticky="n")

cbpediatria=tk.Checkbutton(ventanaRegDoc,text="pediatria",variable=pediatria)

cbpediatria.grid(row=8,column=1,sticky="n")

cboftalmologia=tk.Checkbutton(ventanaRegDoc,text="oftalmologia",variable=oftalmologia)


cboftalmologia.grid(row=9,column=1,sticky="n")

#Acción: registrar datos

def registrarDatos():

especialidades=[]

if cardiologia.get():

especialidades.append("cardiologia")

if pediatria.get():

especialidades.append("pediatria")

if oftalmologia.get():

especialidades.append("oftalmologia")

if len(especialidades)>0:

especialidades=','.join(especialidades)

else:

especialidades='Ninguna'






horLabel=tk.Label(ventanaRegDoc,text="horario:",bg="lightblue")

horLabel.grid(row=10,column=0,padx=10,pady=5,sticky="n")

mañana=tk.BooleanVar()

tarde=tk.BooleanVar()

noche=tk.BooleanVar()

cbmañana=tk.Checkbutton(ventanaRegDoc,text="mañana",variable=mañana)

cbmañana.grid(row=11,column=1,sticky="n")

cbtarde=tk.Checkbutton(ventanaRegDoc,text="tarde",variable=tarde)

cbtarde.grid(row=12,column=1,sticky="n")

cbnoche=tk.Checkbutton(ventanaRegDoc,text="noche",variable=noche)

cbnoche.grid(row=13,column=1,sticky="n")

#Acción: registrar datos

def registrarDatos():

horarios=[]

if mañana.get():

horarios.append("mañana")

if tarde.get():

horarios.append("tarde")

if noche.get():

horarios.append("noche")

if len(horarios)>0:

horarios=','.join(horarios)

else:

horarios='Ninguno'