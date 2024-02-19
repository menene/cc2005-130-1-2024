import turtle

window = turtle.Screen()

tudis = turtle.Turtle()



tudis.forward(100)
tudis.backward(250)
tudis.right(45)
tudis.forward(200)
tudis.left(90)
tudis.forward(230)

pos = tudis.position()
print(pos)


tudis.up()
tudis.goto(100, 300)
tudis.down()

#tudis.clear()
#tudis.reset()

tudis.pensize(10)

tudis.home()





window.exitonclick()
turtle.Terminator()