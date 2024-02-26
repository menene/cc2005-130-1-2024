import turtle

# import figuras
# from figuras import *
# from figuras import cuadrado
from figuras import cuadrado, cuadrado_relleno


window = turtle.Screen()
tudis = turtle.Turtle()
tudis.shape("turtle")
tudis.color("red")
tudis.speed(10)


#figuras.cuadrado(tudis, 150)
cuadrado(tudis, 250)
cuadrado_relleno(tudis, 150, "red")

window.exitonclick()
turtle.Terminator()


