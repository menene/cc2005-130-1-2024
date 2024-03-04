import turtle
import figurasfor

window = turtle.Screen()
tudis = turtle.Turtle()
tudis.shape("turtle")
tudis.color("red")
tudis.speed(10)

opcion = ""
#edad = int(input("Ingresa tu edad: "))

largo = 90

# figuras.poligono(tudis, 5, largo)
# figuras.quitate(tudis, -100, -100)
# figuras.poligono(tudis, 6, largo)
# figuras.quitate(tudis, 100, 100)
# figuras.poligono(tudis, 7, largo)
# figuras.quitate(tudis, -100, 100)
# figuras.poligono(tudis, 8, largo)
# figuras.quitate(tudis, 100, -100)
# figuras.poligono(tudis, 12, largo)
while opcion != "salir":
    opcion = input("Qué figura quieres dibujar (salir para terminar): ")
    
    if opcion == "triangulo":
        figurasfor.poligono(tudis, 3, largo)
    elif opcion == "cuadrado":
        figurasfor.poligono(tudis, 4, largo)
    elif opcion == "pentagono":
        figurasfor.poligono(tudis, 5, largo)
    elif opcion == "hexagono":
        figurasfor.poligono(tudis, 6, largo)
    elif opcion == "heptagono":
        figurasfor.poligono(tudis, 7, largo)
    elif opcion == "salir":
        print("Hasta luego :)")
        
        turtle.Terminator()
    else:
        print("Figura no reconocida...")
        lados = int(input("¿Cuantos lados tiene tu figura?"))
        figurasfor.poligono(tudis, lados, largo)



window.exitonclick()
turtle.Terminator()