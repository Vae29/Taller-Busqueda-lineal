##################- Priemer ejercicio - ###########################
def busqueda_lineal_simple (lista, objetivo):
    for i in range (len (lista)):
        if lista [i] == objetivo:
            return i
    return -1

#Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print(f"El número 25 esta en la posición ||{busqueda_lineal_simple(numeros, 25)}|| de la lista")  
print(f"El número 99 no esta en la lista, resultado: {busqueda_lineal_simple(numeros, 99)}") 





##################- Segundo ejercicio -###########################
#busqueda en lista de productos

productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
]


def buscar_producto_por_nombre(productos, nombre_objetivo):
    for producto in productos:
        if producto['nombre'] == nombre_objetivo:
            return producto
    return None

def buscar_producto_por_id(productos, id_objetivo):
    for producto in productos:
        if producto['id'] == id_objetivo:
            return producto
    return None

def buscar_productos_por_categoria(productos, categoria_objetivo):
    productos_encontrados = []
    for producto in productos:
        if producto['categoria'] == categoria_objetivo:
            productos_encontrados.append(producto)
    return productos_encontrados


#Ejemplo de uso

#buscar producto por nombre
producto_buscado_nombre = buscar_producto_por_nombre(productos, 'MacBook Air M3')
if producto_buscado_nombre:
    print("\nProducto encontrado:")
    for clave, valor in producto_buscado_nombre.items():
        print(f" - {clave.capitalize()}: {valor}")
else:
    print("Producto no encontrado.")

#buscar producto por id
producto_buscado_id = buscar_producto_por_id(productos, 4)
if producto_buscado_id:
    print("\nProducto encontrado por id:")
    for clave, valor in producto_buscado_id.items():
        print(f" - {clave.capitalize()}: {valor}")
else:
    print("Producto no encontrado.")

#buscar producto por categoria
producto_buscado_categoria = buscar_productos_por_categoria(productos, 'Smartphone')
if producto_buscado_categoria:
    print("\nProductos encontrados en la categoría 'Smartphone':")
    for producto in producto_buscado_categoria:
        for clave, valor in producto.items():
            print(f" - {clave.capitalize()}: {valor}")
        print("-----")
else:
    print("No se encontraron productos en esa categoría.")




##################- Tercer ejercicio -###########################
#Busqueda de empleados

empleados = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True}
]
    
def buscar_por_nombre_completo(empleados, nombre_objetivo, apellido_objetivo):
    for empleado in empleados:
        if empleado['nombre'] == nombre_objetivo and empleado['apellido'] == apellido_objetivo:
            return empleado
    return None

def buscar_por_departamento(empleados, departamento_objetivo):
    empleados_encontrados = []
    for empleado in empleados:
        if empleado['departamento'] == departamento_objetivo:
            empleados_encontrados.append(empleado)
    return empleados_encontrados

def buscar_por_estado_activo(empleados, estado_activo=True):
    empleados_encontrados = []
    for empleado in empleados:
        if empleado['activo'] == estado_activo:
            empleados_encontrados.append(empleado)
    return empleados_encontrados
        
#Ejemplos de uso
#Buscar por nombre completo
empleado_buscado_nombre = buscar_por_nombre_completo(empleados, 'Carlos', 'López')
if empleado_buscado_nombre:
    print("\nEmpleado encontrado por nombre completo:")
    for clave, valor in empleado_buscado_nombre.items():
        print(f" - {clave.capitalize()}: {valor}")
else:
    print("Empleado no encontrado.")

#Buscar por departamento
empleados_buscados_departamento = buscar_por_departamento(empleados, 'Ventas')
if empleados_buscados_departamento:
    print("\nEmpleados encontrados en el departamento 'Ventas':")
    for empleado in empleados_buscados_departamento:
        for clave, valor in empleado.items():
            print(f" - {clave.capitalize()}: {valor}")
        print("-----")
else:
    print("No se encontraron empleados en ese departamento.")

#Buscar por estado activo
empleados_buscados_activos = buscar_por_estado_activo(empleados, True)
if empleados_buscados_activos:
    print("\nEmpleados activos:")
    for empleado in empleados_buscados_activos:
        for clave, valor in empleado.items():
            print(f" - {clave.capitalize()}: {valor}")
        print("-----")
else:
    print("No se encontraron empleados activos.")


##################- Cuarto ejercicio -###########################
#Busqueda por disponibilidad

#reutilizo la lista de productos del segundo ejercicio

def buscar_productos_disponibles(productos):
    productos_disponibles = []
    for producto in productos:
        if (producto['disponible'] == True) or (producto['stock'] > 0):
            productos_disponibles.append(producto)
    return productos_disponibles

def buscar_productos_por_rango_de_precio(productos, precio_minimo, precio_maximo):
    productos_encontrados = []
    for producto in productos:
        if precio_minimo <= producto['precio'] <= precio_maximo:
            productos_encontrados.append(producto)
    return productos_encontrados

def buscar_productos_por_marca(productos, marca_objetivo):
    productos_encontrados = []
    for producto in productos:
        if producto['marca'] == marca_objetivo:
            productos_encontrados.append(producto)
    return productos_encontrados

def contar_productos_en_categoria(productos, categoria_objetivo):
    contador = 0
    for producto in productos:
        if producto['categoria'] == categoria_objetivo:
            contador += 1
    return contador

#ejemplos de uso
#Buscar productos disponibles
productos_disponibles = buscar_productos_disponibles(productos)
if productos_disponibles:
    print("\nProductos disponibles:\n")
    for producto in productos_disponibles:
        for clave, valor in producto.items():
            print(f" - {clave.capitalize()}: {valor}")
        print("-----")
else:
    print("No hay productos disponibles.")

#buscar productos por rango de precio
productos_en_rango = buscar_productos_por_rango_de_precio(productos, 500, 1300)
if productos_en_rango:
    print("\nProductos en el rango de precio 500 - 1300:\n")
    for producto in productos_en_rango:
        for clave, valor in producto.items():
            print(f" - {clave.capitalize()}: {valor}")
        print("-----")
else:
    print("No se encontraron productos en ese rango de precio.")

#buscar productos por marca
productos_marca = buscar_productos_por_marca(productos, 'Apple')
if productos_marca:
    print("\nProductos de la marca 'Apple':\n")
    for producto in productos_marca:
        for clave, valor in producto.items():
            print(f" - {clave.capitalize()}: {valor}")
        print("-----")
else:
    print("No se encontraron productos de esa marca.")

    