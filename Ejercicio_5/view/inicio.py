import tkinter as tk
from tkinter import *
from .menu import Menu

class Inicio:
    def mostrar_menu(self):
        Menu()

    def salir(self):
        self.ventana.destroy()

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(width=440, height=300,background="#f7e0f9")
        self.ventana.title("Ventana de Inicio - TechStore")

        self.label_bienvenida = Label(self.ventana, text="Bienvenido a TechStore", font=("", 16, "bold"), background="#f7e0f9")
        self.label_bienvenida.place(relx=0.5, y=50, anchor="center")

        self.btn_menu=tk.Button(self.ventana, text="Ver menú principal", command=self.mostrar_menu, bg="#823d8b", fg="white", font=("", 12))
        self.btn_menu.place(relx=0.5, y=150, anchor="center", width=200)

        self.btn_salir=tk.Button(self.ventana, text="Salir", command=self.salir, bg="#ffffff", fg="#823d8b", font=("", 12))
        self.btn_salir.place(relx=0.5, y=220, anchor="center", width=200)



        self.ventana.mainloop()