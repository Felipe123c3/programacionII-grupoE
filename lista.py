import tkinter as tk
from tkinter import messagebox
ventana=tk.Tk()
ventana.title("ejemplo listbox")
sintomasLabel=tk.Label(ventana, text= "sintomas")
sintomasLabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")
#crear listbox
lista=tk.Listbox(ventana, selectmode=tk.SINGLE)
lista.insert(1, "dolor de cabeza")
lista.insert(2, "fiebre")
lista.insert(3, "tos")
lista.insert(4, "fatiga")
lista.insert(5, "dificultad para respirar")
lista.grid(row=0, column=1, pady=10, sticky="we")
#boton para mostrar selccion
def mostrar():
    seleccionado=lista.get(lista.curselection())
    tk.messagebox.showinfo("seleccion", f"Has elegido: {seleccionado}")
boton=tk.Button(ventana, text="Mostrar seleccion", command=mostrar)
boton.grid(row=1, column=0, padx=10, pady=10)

ventana.mainloop()