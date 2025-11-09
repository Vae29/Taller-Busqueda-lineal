import tkinter as tk
from tkinter import *
from .menu_productos import ProductosMenu
from .menu_empleados import EmpleadosMenu
class Menu:
    def buscar_productos(self):
        ProductosMenu(self.ventana)

    def buscar_empleados(self):
        EmpleadosMenu(self.ventana)

    def devolver(self):
        self.ventana.destroy()
        
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.attributes('-topmost', True)
        self.ventana.config(width=350, height=300, background="#f7e0f9")
        self.ventana.title("Ventana de Menú - TechStore")

        self.bandera=False

        self.label_Menu = Label(self.ventana, text="Menú principal", font=("", 16, "bold"), background="#f7e0f9")
        self.label_Menu.place(relx=0.5, y=50, anchor="center")

        self.btn_productos=tk.Button(self.ventana, text="Buscar Productos", command=self.buscar_productos, bg="#823d8b", fg="white", font=("", 12))
        self.btn_productos.place(relx=0.5, y=150, anchor="center", width=200)

        self.btn_empleados=tk.Button(self.ventana, text="Buscar Empleados", command=self.buscar_empleados, bg="#823d8b", fg="white", font=("", 12))
        self.btn_empleados.place(relx=0.5, y=200, anchor="center", width=200)

        self.btn_salir=tk.Button(self.ventana, text="Salir", command=self.devolver, bg="#ffffff", fg="#823d8b", font=("", 12))
        self.btn_salir.place(relx=0.5, y=250, anchor="center", width=200)

        self.ventana.mainloop()

