def poligono(tortu, lados, largo):
    angulo = 360 / lados
    
    for i in range(lados):
        tortu.forward(largo)
        tortu.left(angulo)