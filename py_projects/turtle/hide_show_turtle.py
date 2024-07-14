import turtle

wn = turtle.Screen()

turtle.speed(1)

turtle.hideturtle()
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()
turtle.circle(100)

turtle.showturtle()
turtle.penup()
turtle.goto(-55, -300)
turtle.pendown()
turtle.circle(15)

turtle.hideturtle()
turtle.penup()
turtle.goto(55, -300)
turtle.pendown()
turtle.circle(15)

turtle.showturtle()
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(60)

turtle.hideturtle()
turtle.penup()
turtle.goto(60, -40)
turtle.pendown()
turtle.forward(50)

turtle.showturtle()
turtle.penup()
turtle.goto(-60, -40)
turtle.pendown()
turtle.forward(-50)

turtle.hideturtle()
turtle.penup()
turtle.goto(0, 20)
turtle.pendown()
turtle.circle(30)

turtle.showturtle()
turtle.penup()
turtle.goto(15, 50)
turtle.pendown()
turtle.circle(5)

turtle.hideturtle()
turtle.penup()
turtle.goto(-15, 50)
turtle.pendown()
turtle.circle(5)

wn.mainloop()