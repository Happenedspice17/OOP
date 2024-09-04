"""Ejercicio 1:
Una tienda de ropa lleva un registro de sus ventas diarias en una lista de diccionarios. 
Cada diccionario representa una venta e incluye el nombre del cliente, la prenda vendida 
(como un diccionario con detalles como tipo de prenda, tamaño, y precio), 
y si el cliente utilizó un cupón de descuento.

Datos:
ventas = [
    {"cliente": "Ana", "prenda": {"tipo": "Camiseta", "tamaño": "M", "precio": 200}, "descuento": 10},
    {"cliente": "Carlos", "prenda": {"tipo": "Pantalón", "tamaño": "L", "precio": 400}},
    {"cliente": "Lucía", "prenda": {"tipo": "Vestido", "tamaño": "S", "precio": 500}, "descuento": 15},
    {"cliente": "Luis", "prenda": {"tipo": "Camiseta", "tamaño": "M", "precio": 200}},
    {"cliente": "María", "prenda": {"tipo": "Falda", "tamaño": "M", "precio": 250}, "descuento": 5},
]

El programa debe de:
1. Calcular el total recaudado por la tienda después y antes  de aplicar los descuentos.
2. Desglosar el total recaudado por tipo de prenda (Camiseta, Pantalón, etc.).
3. Determinar cuántos clientes utilizaron un cupón de descuento.
4. Desglosar cuantas prendas se vendieron de cada una.
"""

# Datos de ventas
ventas = [
    # Cada venta es un diccionario que contiene el nombre del cliente, la prenda (con tipo, tamaño y precio) y, opcionalmente, un descuento.
    {"cliente": "Ana", "prenda": {"tipo": "Camiseta", "tamaño": "M", "precio": 200}, "descuento": 10},
    {"cliente": "Carlos", "prenda": {"tipo": "Pantalón", "tamaño": "L", "precio": 400}},
    {"cliente": "Lucía", "prenda": {"tipo": "Vestido", "tamaño": "S", "precio": 500}, "descuento": 15},
    {"cliente": "Luis", "prenda": {"tipo": "Camiseta", "tamaño": "M", "precio": 200}},
    {"cliente": "María", "prenda": {"tipo": "Falda", "tamaño": "M", "precio": 250}, "descuento": 5},
]

# Inicialización de variables
total_sin_descuento = 0  # Variable para acumular el total recaudado sin aplicar descuentos
total_con_descuento = 0  # Variable para acumular el total recaudado después de aplicar descuentos
tipo_prenda_total = {}   # Diccionario para contar la cantidad de prendas vendidas por tipo
total_clientes_descuento = 0  # Variable para contar cuántos clientes usaron un cupón de descuento
cantidad_prendas = {}    # Diccionario para contar la cantidad total de cada tipo de prenda vendida

# Procesamiento de ventas
for venta in ventas:
    # Obtener el precio de la prenda
    precio = venta["prenda"]["precio"]  # Accedemos al precio de la prenda en la venta actual
    total_sin_descuento += precio  # Acumulamos el precio en el total sin descuento

    # Verificar si hay descuento
    if "descuento" in venta:
        descuento = venta["descuento"]  # Si hay descuento, lo obtenemos
        precio_con_descuento = precio * (1 - descuento / 100)  # Calculamos el precio con descuento aplicado
        total_con_descuento += precio_con_descuento  # Acumulamos el precio con descuento en el total con descuento
        total_clientes_descuento += 1  # Contamos el cliente que usó un cupón de descuento
    else:
        total_con_descuento += precio  # Si no hay descuento, simplemente acumulamos el precio en el total con descuento

    # Contar las prendas por tipo
    tipo_prenda = venta["prenda"]["tipo"]  # Obtenemos el tipo de prenda de la venta actual
    if tipo_prenda not in tipo_prenda_total:
        tipo_prenda_total[tipo_prenda] = 0  # Inicializamos el contador para el tipo de prenda si no existe en el diccionario
    tipo_prenda_total[tipo_prenda] += 1  # Incrementamos el contador para el tipo de prenda en el diccionario

    # Contar las prendas en total
    if tipo_prenda not in cantidad_prendas:
        cantidad_prendas[tipo_prenda] = 0  # Inicializamos el contador total para el tipo de prenda si no existe en el diccionario
    cantidad_prendas[tipo_prenda] += 1  # Incrementamos el contador total para el tipo de prenda en el diccionario

# Resultados
print("Total recaudado antes de aplicar descuentos: $", total_sin_descuento)  # Imprimimos el total sin descuentos
print("\nTotal recaudado después de aplicar descuentos: $", total_con_descuento)  # Imprimimos el total con descuentos aplicados
print("\nTotal clientes que utilizaron un cupón de descuento:", total_clientes_descuento)  # Imprimimos el número de clientes que usaron un cupón
print("\nDesglose del total recaudado por tipo de prenda:")  # Imprimimos un encabezado para el desglose por tipo de prenda

# Ciclo for para ver cada tipo y cantidad en los items del diccionario "Tipo_prenda_total"
for tipo, cantidad in tipo_prenda_total.items():
    print(f"{tipo}: {cantidad} prenda(s) vendida(s)")  # Imprimimos la cantidad de cada tipo de prenda vendida
# Ciclo for para ver cada tipo y cantidad en los items del diccionario "Tipo_prenda_total"

print("\nCantidad de cada tipo de prenda vendida:")  # Imprimimos un encabezado para la cantidad total de cada tipo de prenda
# Ciclo for para ver cada tipo y cantidad en los items del diccionario "cantidad_prendas"
for tipo, cantidad in cantidad_prendas.items():
    print(f"{tipo}: {cantidad} prenda(s)")  # Imprimimos la cantidad total de cada tipo de prenda vendida
