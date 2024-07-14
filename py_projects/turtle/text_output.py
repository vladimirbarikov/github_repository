import turtle

wn = turtle.Screen()
turtle.setup(400, 300)

turtle.write("Hi, world!")

turtle.penup()
turtle.hideturtle()

turtle.goto(-120,120)
turtle.write('Top left')

turtle.goto(70,-120)
turtle.write('Bottom right')

wn.mainloop()