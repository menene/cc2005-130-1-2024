def poligono(tortu, lados, largo):
    angulo = 360 / lados
    
    vuelta = 1
    while vuelta <= lados:
        tortu.forward(largo)
        tortu.left(angulo)
        
        vuelta = vuelta + 1
    
def quitate(tortu, x, y):
    tortu.up()
    tortu.goto(x, y)
    tortu.down()
    
    
    
