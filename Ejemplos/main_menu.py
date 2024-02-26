import turtle
import figuras

window = turtle.Screen()
tudis = turtle.Turtle()
tudis.shape("turtle")
tudis.color("red")
tudis.speed(10)

opcion = "lo que sea"

while opcion != "salir":
    opcion = input("Qué figura quieres dibujar (salir para terminar): ")
    
    if opcion == "cuadrado":
        figuras.cuadrado(tudis, 150)
    elif opcion == "triangulo":
        figuras.triangulo(tudis, 250)
    elif opcion == "salir":
        print("Hasta luego :)")
    else:
        print("Figura no reconocida... intentalo nuevamente")
        
        
window.exitonclick()
turtle.Terminator()