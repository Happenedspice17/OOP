import json
import os.path as path

# miDiccionario = {
#     "llave1" : "valor",
#     "llave 2": 123
# }

# print(miDiccionario["llave1"])
# print(miDiccionario["llave 2"])

# if not path.exists("C:/Users/emili/Documents/OOP/04-SQLite/datos.json"):
#     file = open("C:/Users/emili/Documents/OOP/04-SQLite/datos.json", "x")
#     file.flush()
#     file.close()

# file = open("C:/Users/emili/Documents/OOP/04-SQLite/datos.json", "w")
# file.write(json.dumps(miDiccionario)) #! dump string

# file.flush()
# file.close()

# file = open("C:/Users/emili/Documents/OOP/04-SQLite/datos.json", "r")
# miDic2 = json.load(file)

# print(miDic2)

misUsuarios = {}

n_users = int(input("Cuantos usuarios quieres agregar?\n"))

for user in range(n_users):
    Id = int(input("ID del usuario: "))
    nombre= input("Nombre del usuario ")

    misUsuarios[Id] = {"nombre": nombre, "id": Id}
    
    # misUsuarios[Id] = nombre

file = None
ruta = "C:/Users/emili/Documents/OOP/04-SQLite/datos.json"

if path.exists(ruta):
    file = open(ruta, "w")
else:
    file = open(ruta, "x")

file.write(json.dumps(misUsuarios))