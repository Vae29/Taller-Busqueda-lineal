import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog

class ProductosMenu:

    def buscar_por_nombre(self):
        opcion = simpledialog.askstring("Buscar por Nombre", "Ingrese el nombre del producto:")
        if opcion:
            for producto in self.productos:
                if opcion.lower() in producto['nombre'].lower():
                    messagebox.showinfo("Producto Encontrado", f"ID: {producto['id']}\nNombre: {producto['nombre']}\nMarca: {producto['marca']}\nCategoría: {producto['categoria']}\nPrecio: ${producto['precio']}\nStock: {producto['stock']}\nDisponible: {'Sí' if producto['disponible'] else 'No'}")
                    return
        else:
            messagebox.showwarning("Entrada Vacía", "No se ingresó ningún nombre de producto.")
            return
            
    def buscar_por_marca(self):
        opcion = simpledialog.askstring("Buscar por Marca", "Ingrese la marca del producto:")
        texto=""
        productos_encontrados = []
        if opcion:          
            for producto in self.productos:
                if producto['marca'].lower() == opcion.lower():
                    productos_encontrados.append(producto)
                    texto+=f"ID: {producto['id']}\nNombre: {producto['nombre']}\nMarca: {producto['marca']}\nCategoría: {producto['categoria']}\nPrecio: ${producto['precio']}\nStock: {producto['stock']}\nDisponible: {'Sí' if producto['disponible'] else 'No'}\n\n"
            if productos_encontrados:
                messagebox.showinfo("Productos Encontrados", texto)
            else:
                messagebox.showinfo("No Encontrado", "No se encontraron productos de esa marca.")
        else:
            messagebox.showwarning("Entrada Vacía", "No se ingresó ningún nombre de producto.")
            return
        
    def buscar_por_categoria(self):
        opcion = simpledialog.askstring("Buscar por Categoría", "Seleccione un número:\n1. Smartphone\n2. Laptop\n3. Audífonos")
        if opcion:
            categoria=""
            if opcion=="1":
                categoria="Smartphone"
            elif opcion=="2":
                categoria="Laptop"
            elif opcion=="3":
                categoria="Audífonos"
            else:
                messagebox.showwarning("Opción Inválida", "No se seleccionó una categoría válida.")
                return
            texto=""
            productos_encontrados = []
            for producto in self.productos:
                if producto['categoria'].lower() == categoria.lower():
                    productos_encontrados.append(producto)
                    texto+=f"ID: {producto['id']}\nNombre: {producto['nombre']}\nMarca: {producto['marca']}\nCategoría: {producto['categoria']}\nPrecio: ${producto['precio']}\nStock: {producto['stock']}\nDisponible: {'Sí' if producto['disponible'] else 'No'}\n\n"
            if productos_encontrados:
                messagebox.showinfo("Productos Encontrados", texto)
            else:
                messagebox.showinfo("No Encontrado", "No se encontraron productos en esa categoría.")
        else:
            messagebox.showwarning("Entrada Vacía", "No se ingresó ningún nombre de producto.")
            return
    
    def buscar_productos_disponibles(self):
        productos_encontrados = []
        texto=""
        for producto in self.productos:
            if producto['disponible'] == True:
                productos_encontrados.append(producto)
                texto+=f"ID: {producto['id']}\nNombre: {producto['nombre']}\nMarca: {producto['marca']}\nCategoría: {producto['categoria']}\nPrecio: ${producto['precio']}\nStock: {producto['stock']}\nDisponible: {'Sí' if producto['disponible'] else 'No'}\n\n"
        if productos_encontrados:
            messagebox.showinfo("Productos Disponibles", texto)
        else:
            messagebox.showinfo("No Encontrado", "No hay productos disponibles.")

    def salir(self):
        self.ventana_menu_principal.destroy()       

    def __init__(self, ventana):
        self.ventana_menu_principal=ventana
        self.ventana = tk.Toplevel(self.ventana_menu_principal)
        self.ventana.resizable(0,0)
        self.ventana.attributes('-topmost', True)
        self.ventana.config(width=350, height=400, background="#f7e0f9")
        self.ventana.title("Ventana de Productos - TechStore")

        self.label_bienvenida = Label(self.ventana, text="Gestión de Productos", font=("", 16, "bold"), background="#f7e0f9")
        self.label_bienvenida.place(relx=0.5, y=50, anchor="center")

        self.btn_buscar_nombre=tk.Button(self.ventana, text="Buscar por nombre", command=self.buscar_por_nombre, bg="#823d8b", fg="white", font=("", 12))
        self.btn_buscar_nombre.place(relx=0.5, y=150, anchor="center", width=200)

        self.btn_buscar_marca=tk.Button(self.ventana, text="Buscar por marca", command=self.buscar_por_marca, bg="#823d8b", fg="white", font=("", 12))
        self.btn_buscar_marca.place(relx=0.5, y=200, anchor="center", width=200)

        self.btn_buscar_categoria=tk.Button(self.ventana, text="Buscar por categoría", command=self.buscar_por_categoria, bg="#823d8b", fg="white", font=("", 12))
        self.btn_buscar_categoria.place(relx=0.5, y=250, anchor="center", width=200)

        self.btn_disponible=tk.Button(self.ventana, text="Productos disponibles", command=self.buscar_productos_disponibles, bg="#823d8b", fg="white", font=("", 12))
        self.btn_disponible.place(relx=0.5, y=300, anchor="center", width=200)

        self.btn_salir=tk.Button(self.ventana, text="Salir", command=self.salir, bg="#ffffff", fg="#823d8b", font=("", 12))
        self.btn_salir.place(relx=0.5, y=350, anchor="center", width=200)

        self.productos = [
            {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
            {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
            {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
            {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
            {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
        ]

        self.ventana.mainloop()