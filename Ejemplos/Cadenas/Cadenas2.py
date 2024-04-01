"""
cadena = "Hola Mundo"

for letra in cadena:
    print(letra)
"""

"""
cadena = "Hola Mundo"

indice = 0
while indice < len(cadena):
    print(cadena[indice])
    indice += 1
"""

cadena = "Hola Mundo"
control = "HIou"
#print("H" in control)
for letra in cadena:
    if letra in control:
        print("Letra", letra, "se encuentra en el control")
