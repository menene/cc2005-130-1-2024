calificacion = 96

# menos de 61 = perdio
# de 61 a 85 = gano
# de 85 a 95 = magna cum laude
# de 95 a 100 = suma cum laude 


if calificacion < 61:
    print("Perdiste")
elif calificacion > 85 and calificacion < 95:
    print("Magna Cum Laude")
elif calificacion >= 95:
    print("Suma Cum Laude")
else:
    print("Ganaste")



if calificacion < 6:
    print("Perdiste")
else:
    if calificacion > 85:
        if calificacion >= 95:
            print("Suma Cum Laude")
        else:
            print("Magna Cum Laude")
    else:
        print("Ganaste")



