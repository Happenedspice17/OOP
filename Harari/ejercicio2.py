"""Ejercicio 2:

Una tienda lleva un registro de las compras realizadas por sus clientes en un día utilizando un diccionario. Cada entrada en el diccionario representa un cliente e incluye su nombre y una lista de productos que compró. Cada producto en la lista es otro diccionario que contiene el nombre del producto y su precio.

Datos:
compras = {
    "Cliente1": {
        "nombre": "Juan",
        "productos": [
            {"producto": "Pan", "precio": 20},
            {"producto": "Leche", "precio": 30}
        ]
    },
    "Cliente2": {
        "nombre": "María",
        "productos": [
            {"producto": "Huevos", "precio": 25},
            {"producto": "Aceite", "precio": 50}
        ]
    },
    "Cliente3": {
        "nombre": "Carlos",
        "productos": [
            {"producto": "Huevos", "precio": 40},
            {"producto": "Queso", "precio": 60}
        ]
    }
}
El programa debe de:

Calcular el Total Gastado por Cada Cliente:

El programa debe calcular el total de dinero que cada cliente gastó en sus compras.
Determinar el Producto Más Caro Comprado por Cada Cliente:

El programa debe identificar cuál fue el producto más caro que cada cliente compró.
Calcular el Total Recaudado por la Tienda:

El programa debe sumar todas las compras realizadas por los clientes para obtener el total recaudado por la tienda en ese día.
Determinar cuál es el producto más comprado y el que más dinero ha generado
El programa debe poder saber qué producto se ha vendido más ( el que más apariciones ha tenido) y el que más dinero ha generado. (No necesariamente debe de ser el mismo producto)
"""

# Datos de compras
compras = {
    # Cada cliente es una entrada en el diccionario, con su nombre y una lista de productos comprados.
    "Cliente1": {
        "nombre": "Juan",
        "productos": [
            {"producto": "Pan", "precio": 20},
            {"producto": "Leche", "precio": 30}
        ]
    },
    "Cliente2": {
        "nombre": "María",
        "productos": [
            {"producto": "Huevos", "precio": 25},
            {"producto": "Aceite", "precio": 50}
        ]
    },
    "Cliente3": {
        "nombre": "Carlos",
        "productos": [
            {"producto": "Huevos", "precio": 40},
            {"producto": "Queso", "precio": 60}
        ]
    }
}

# Inicialización de variables
total_recaudado = 0  # Variable para acumular el total de dinero recaudado por la tienda
producto_mas_comprado = {}  # Diccionario para contar la cantidad de cada producto comprado
producto_mas_generado = {}  # Diccionario para acumular el total de dinero generado por cada producto

# Procesamiento de compras
for cliente_id, cliente_info in compras.items():
    # Obtener el nombre del cliente y la lista de productos comprados
    nombre_cliente = cliente_info["nombre"]
    productos = cliente_info["productos"]
    
    # Calcular el total gastado por el cliente
    total_cliente = sum(producto["precio"] for producto in productos)  # Suma de los precios de los productos del cliente
    print(f"{nombre_cliente} gastó un total de: ${total_cliente}")  # Imprime el total gastado por el cliente
    
    # Determinar el producto más caro comprado por el cliente
    producto_mas_caro = max(productos, key=lambda x: x["precio"])  # Encuentra el producto con el precio máximo
    print(f"Producto más caro comprado por {nombre_cliente}: {producto_mas_caro['producto']} (${producto_mas_caro['precio']})")  # Imprime el producto más caro
    
    # Acumulamos el total recaudado por la tienda
    total_recaudado += total_cliente  # Añadimos el total del cliente al total general
    
    # Contar la cantidad de cada producto y el total generado por cada producto
    for producto in productos:
        nombre_producto = producto["producto"]
        precio_producto = producto["precio"]
        
        # Inicializamos los contadores si el producto aún no está en los diccionarios
        if nombre_producto not in producto_mas_comprado:
            producto_mas_comprado[nombre_producto] = 0  # Inicializa el contador de cantidad del producto
            producto_mas_generado[nombre_producto] = 0  # Inicializa el acumulador de dinero del producto
        
        producto_mas_comprado[nombre_producto] += 1  # Incrementa la cantidad de veces que se ha comprado el producto
        producto_mas_generado[nombre_producto] += precio_producto  # Añade el precio del producto al total generado por el mismo

# Determinar el producto más comprado
producto_mas_comprado_nombre = max(producto_mas_comprado, key=producto_mas_comprado.get)  # Encuentra el producto con la mayor cantidad de compras
cantidad_mas_comprado = producto_mas_comprado[producto_mas_comprado_nombre]  # Obtiene la cantidad de veces que se compró el producto más comprado

# Determinar el producto que más dinero ha generado
producto_mas_generado_nombre = max(producto_mas_generado, key=producto_mas_generado.get)  # Encuentra el producto que ha generado más dinero
dinero_mas_generado = producto_mas_generado[producto_mas_generado_nombre]  # Obtiene el total de dinero generado por el producto más generador

# Resultados
print("\nTotal recaudado por la tienda: $", total_recaudado)  # Imprime el total recaudado por la tienda
print("\nProducto más comprado:")  # Imprime el encabezado para el producto más comprado
print(f"{producto_mas_comprado_nombre}: {cantidad_mas_comprado} vez/veces")  # Imprime el nombre y la cantidad del producto más comprado

print("\nProducto que más dinero ha generado:")  # Imprime el encabezado para el producto que más dinero ha generado
print(f"{producto_mas_generado_nombre}: ${dinero_mas_generado}")  # Imprime el nombre y el total de dinero generado por el producto más generador
