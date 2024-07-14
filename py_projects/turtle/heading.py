import turtle

wn = turtle.Screen()

print(turtle.heading())  # показать направление черепахи
turtle.setheading(180)  # установить направление черепахи на 180 градусов
print(turtle.heading())  # показать направление черепахи

wn.mainloop()