import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog

class EmpleadosMenu:
    def buscar_por_nombre_completo(self):
        opcion= simpledialog.askstring("Buscar por Nombre Completo", "Ingrese el nombre completo del empleado (Nombre Apellido):")
        if opcion:
            nombre_apellido = opcion.split()
            if len(nombre_apellido) != 2:
                messagebox.showwarning("Entrada Inválida", "Por favor, ingrese el nombre y apellido separados por un espacio.")
                return
            nombre_objetivo = nombre_apellido[0]
            apellido_objetivo = nombre_apellido[1]
            for empleado in self.empleados:
                if empleado['nombre'].lower() == nombre_objetivo.lower() and empleado['apellido'].lower() == apellido_objetivo.lower():
                    messagebox.showinfo("Empleado Encontrado", f"ID: {empleado['id']}\nNombre: {empleado['nombre']}\nApellido: {empleado['apellido']}\nDepartamento: {empleado['departamento']}\nSalario: ${empleado['salario']}\nActivo: {'Sí' if empleado['activo'] else 'No'}")
                    return
            messagebox.showinfo("No Encontrado", "No se encontró ningún empleado con ese nombre completo.")
        else:
            messagebox.showwarning("Entrada Vacía", "No se ingresó ningún nombre de empleado.")
            return

    def buscar_por_departamento(self):
        opcion = simpledialog.askstring("Buscar por Departamento", "Seleccione el departamento:\n1. Ventas\n2. Técnico\n3. Inventario" )
        if opcion:
            departamento=""
            if opcion=="1":
                departamento="Ventas"
            elif opcion=="2":
                departamento="Técnico"
            elif opcion=="3":
                departamento="Inventario"
            else:
                messagebox.showwarning("Opción Inválida", "No se seleccionó una categoría válida.")
                return
            texto=""
            empleados_encontrados = []
            for empleado in self.empleados:
                if empleado['departamento'].lower() == departamento.lower():
                    empleados_encontrados.append(empleado)
                    texto+=f"ID: {empleado['id']}\nNombre: {empleado['nombre']}\nApellido: {empleado['apellido']}\nDepartamento: {empleado['departamento']}\nSalario: ${empleado['salario']}\nActivo: {'Sí' if empleado['activo'] else 'No'}\n\n"
            if empleados_encontrados:
                messagebox.showinfo("Empleados Encontrados", texto)
            else:
                messagebox.showinfo("No Encontrado", "No se encontraron empleados en ese departamento.")
        else:
            messagebox.showwarning("Entrada Vacía", "No se ingresó ningún departamento.")
            return

    def buscar_por_estado_activo(self):
        empleados_encontrados = []
        texto=""
        for empleado in self.empleados:
            if empleado['activo'] == True:
                empleados_encontrados.append(empleado)
                texto+=f"ID: {empleado['id']}\nNombre: {empleado['nombre']}\nApellido: {empleado['apellido']}\nDepartamento: {empleado['departamento']}\nSalario: ${empleado['salario']}\nActivo: {'Sí' if empleado['activo'] else 'No'}\n\n"
        if empleados_encontrados:
            messagebox.showinfo("Empleados Activos", texto)
        else:
            messagebox.showinfo("No Encontrado", "No se encontraron empleados activos.")
        
    def salir(self):
        self.ventana_menu_principal.destroy()

    def __init__(self, ventana):
        self.ventana_menu_principal=ventana
        self.ventana = tk.Toplevel(self.ventana_menu_principal)
        self.ventana.resizable(0,0)
        self.ventana.attributes('-topmost', True)
        self.ventana.config(width=350, height=350, background="#f7e0f9")
        self.ventana.title("Ventana de Empleados - TechStore")

        self.label_bienvenida = Label(self.ventana, text="Gestión de Empleados", font=("", 16, "bold"), background="#f7e0f9")
        self.label_bienvenida.place(relx=0.5, y=50, anchor="center")

        self.btn_buscar_nombre=tk.Button(self.ventana, text="Buscar por nombre", command=self.buscar_por_nombre_completo, bg="#823d8b", fg="white", font=("", 12))
        self.btn_buscar_nombre.place(relx=0.5, y=150, anchor="center", width=200)

        self.btn_buscar_marca=tk.Button(self.ventana, text="Buscar por departamento", command=self.buscar_por_departamento, bg="#823d8b", fg="white", font=("", 12))
        self.btn_buscar_marca.place(relx=0.5, y=200, anchor="center", width=200)

        self.btn_buscar_categoria=tk.Button(self.ventana, text="Buscar por estado activo", command=self.buscar_por_estado_activo, bg="#823d8b", fg="white", font=("", 12))
        self.btn_buscar_categoria.place(relx=0.5, y=250, anchor="center", width=200)

        self.btn_salir=tk.Button(self.ventana, text="Salir", command=self.salir, bg="#ffffff", fg="#823d8b", font=("", 12))
        self.btn_salir.place(relx=0.5, y=300, anchor="center", width=200)

        self.empleados = [
            {'id': 101, 'nombre': 'Ana', 'apellido': 'Garcia', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
            {'id': 102, 'nombre': 'Carlos', 'apellido': 'Lopez', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
            {'id': 103, 'nombre': 'Maria', 'apellido': 'Rodriguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
            {'id': 104, 'nombre': 'Jose', 'apellido': 'Martinez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True}
        ]
        self.ventana.mainloop()