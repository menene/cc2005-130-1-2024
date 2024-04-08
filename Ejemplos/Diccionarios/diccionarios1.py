diccionario = {"llave": "valor"}

diccionario = {
    "codigo": "cc2005",
    "nombre": "Algoritmos",
    "creditos": 6,
#     "codigo": "cc2006",
#     "codigo": "cc2007",
}

diccionario2 = {
    "codigo": "cc2006",
    "nombre": "Química",
    "creditos": 4
}

lista = ["cc2005", "Algoritmos", 6]

print(diccionario)
# print(lista)

# print(lista[0])
# print(diccionario["codigo"])

# MODIFICAR VALORES
diccionario["codigo"] = "cc2006"
print(diccionario)

# AGREGAR UN VALOR A DICCIONARIOS
diccionario["seccion"] = 130
diccionario["catedratico"] = "Erick Marroquín"

print(diccionario)

# ELIMINAR ELEMENTOS DE DICCIONARIO
del diccionario["seccion"]

print(diccionario)

print(diccionario["facultad"])




