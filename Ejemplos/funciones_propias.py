import turtle

def cuadrado(tortuga, lado):
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)
    
def cuadrado_relleno(tortu, l, color):
    tortu.fillcolor(color)
    tortu.begin_fill()

    tortu.forward(l)
    tortu.left(90)
    tortu.forward(l)
    tortu.left(90)
    tortu.forward(l)
    tortu.left(90)
    tortu.forward(l)
    tortu.left(90)
    
    tortu.end_fill()


window = turtle.Screen()
tudis = turtle.Turtle()
tudis.shape("turtle")
tudis.color("red")
tudis.speed(10)


largo = input("Ingrese el largo del cuadrado 1: ")
largo = int(largo)

# Forma vieja e ineficiente
# tudis.forward(largo)
# tudis.left(90)
# tudis.forward(largo)
# tudis.left(90)
# tudis.forward(largo)
# tudis.left(90)
# tudis.forward(largo)
# tudis.left(90)

# tudis.fillcolor("#db6380")
# tudis.begin_fill()
# cuadrado(tudis, largo)
# tudis.end_fill()
cuadrado_relleno(tudis, largo, "#db6380")

largo = input("Ingrese el largo del cuadrado 2: ")
largo = int(largo)

#tudis.fillcolor("purple")
#tudis.begin_fill()
#cuadrado(tudis, largo)
#tudis.end_fill()
cuadrado_relleno(tudis, largo, "purple")

color = input("Ingrese un color: ")
cuadrado_relleno(tudis, 10, color)


cuadrado(tudis, 20)
cuadrado(tudis, 30)
cuadrado(tudis, 40)
cuadrado(tudis, 50)


tudis.up()
tudis.goto(-200, -200)
tudis.down()

tudis.circle(100)

tudis.up()
tudis.goto(200, 200)
tudis.down()


tudis.circle(100, 200)




window.exitonclick()
turtle.Terminator()