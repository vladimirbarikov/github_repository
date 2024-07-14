import turtle

wn = turtle.Screen()

turtle.hideturtle()

turtle.pensize(25)
turtle.pencolor('black')
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

wn.mainloop()