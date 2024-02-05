import math


modo = input("¿Conoces la hipotenusa? ")

if modo == "si":
    c = int(input("Ingresa el valor de la hipotenusa "))
    
    b = input("Ingresa el valor del cateto B ")
    b = int(b)
    
    if c < b:
        print("Lo sentimos pero el cateto B es mayor a la hipotenusa")
    else:
        a = math.sqrt((c * c) - (b * b))
    
        print("El valor del cateto A es:", a)
else:
    a = int(input("Ingresa el valor del cateto A "))
    
    b = input("Ingresa el valor del cateto B ")
    b = int(b)
    
    c = math.sqrt((a * a) + (b * b))
    
    print("El valor de la hipotenusa es:", c)
    