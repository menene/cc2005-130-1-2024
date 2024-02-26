def cuadrado(tortuga, lado):
    '''
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)
    '''
    vuelta = 1
    
    while vuelta <= 4:
        tortuga.forward(lado)
        tortuga.left(90)
        
        vuelta = vuelta + 1
    
def cuadrado_relleno(tortu, l, color):
    tortu.fillcolor(color)
    tortu.begin_fill()
    
    '''
    tortu.forward(l)
    tortu.left(90)
    tortu.forward(l)
    tortu.left(90)
    tortu.forward(l)
    tortu.left(90)
    tortu.forward(l)
    tortu.left(90)
    '''
    
    cuadrado(tortu, l)
    
    tortu.end_fill()
    
def triangulo(tortu, l):
    '''
    tortu.forward(l)
    tortu.left(120)
    tortu.forward(l)
    tortu.left(120)
    tortu.forward(l)
    tortu.left(120)
    '''
    vuelta = 1
    
    while vuelta <= 3:
        tortu.forward(l)
        tortu.left(120)
        
        vuelta = vuelta + 1
    
    