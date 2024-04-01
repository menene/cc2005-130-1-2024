"""
cadena1 = "Hello"
cadena2 = "World"

#print(cadena1 + cadena2)

mensaje = cadena1 + cadena2
print(mensaje)
print(cadena1)
print(cadena2)
"""

#cadena = "HeLLoWoRlD"
#print(len(cadena))

#largo = len(cadena)
#print(largo)

#print(cadena.isalpha())
#print(cadena.isdigit())

# PROBLEMA
#opcion = int(input("ingrese 1, 2 ó 3: "))
"""
opcion = input("ingrese 1, 2 ó 3: ")
if opcion.isdigit():
    opcion = int(opcion)
    
print(opcion, type(opcion))
"""

"""
opcion = ""
while not opcion.isdigit():
    opcion = input("ingrese un número: ")
    
opcion = int(opcion)
print(opcion, type(opcion))
"""

"""
opcion = input("Ingrese 1, 2 o salir para terminar: ")
if opcion == "1":
    print("seleccionaste 1")
elif opcion == "2":
    print("seleccionaste 2")
elif opcion == "salir" or opcion == "SALIR" or opcion == "Salir" or opcion == "SAlir" or opcion == "SALir"or opcion == "SALIr":
    print("adios")
else:
    print("opción inválida")
"""

"""
cadena = "HeLLo WoRlD"
print(cadena.upper())
print(cadena.lower())
print(cadena.title())
print(cadena)
"""

"""
opcion = input("Ingrese 1, 2 o salir para terminar: ")
#opcion.lower() ERROR NO CAMBIA EL VALOR
#opcion = opcion.lower()

if opcion == "1":
    print("seleccionaste 1")
elif opcion == "2":
    print("seleccionaste 2")
elif opcion.lower() == "salir":
    print("adios")
else:
    print("opción inválida")
"""


cadena = "hello world"
"""
print(cadena.count("l"))
print(cadena.count("wo"))
print(cadena.count("world"))

print(cadena.replace("l", "*"))
print(cadena)

print(cadena.find("l"))
print(cadena.rfind("l"))
"""

"""
print(cadena[0])
print(cadena[1])

n = len(cadena)
print(cadena[n - 1])

print(cadena[-1])
"""
