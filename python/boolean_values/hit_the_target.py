# игра "Порази цель"
import turtle

# именованные константы
screen_width = 600      # ширина экрана
screen_height = 600     # высота экрана
target_lleft_x = 100    # левая нижняя координата x цели
target_lleft_y: int = 250    # левая нижняя координата y цели
target_width = 25       # ширина цели
force_factor = 30       # фактор роизвольной силы
projectile_speed = 1    # скорость анимации снаряда
north = 90              # угол северного направления
south = 270             # угол южного направления
east = 0                # угол восточного направления
west = 180              # угол западного направления

# настроить окно
turtle.setup(screen_width, screen_height)

# нарисовать цель
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(target_lleft_x, target_lleft_y)
turtle.pendown()
turtle.setheading(east)
turtle.forward(target_width)
turtle.setheading(north)
turtle.forward(target_width)
turtle.setheading(west)
turtle.forward(target_width)
turtle.setheading(south)
turtle.forward(target_width)
turtle.penup()

# центрировать черепаху
turtle.goto(0, 0)
turtle.setheading(east)
turtle.showturtle()
turtle.speed(projectile_speed)

# получить угол и силу от пользователя
angle = float(input('Введите угол снаряда: '))
force = float(input('Введите пусковую силу (1 - 10): '))

# рассчитать расстояние
distance = force * force_factor

# задать направление
turtle.setheading(angle)

# запустить снаряд
turtle.pendown()
turtle.forward(distance)

# снаряд поразил цель
if (turtle.xcor() >= target_lleft_x and
    turtle.xcor() <= (target_lleft_x + target_width) and
    turtle.ycor() >= target_lleft_y and
    turtle.ycor() <= (target_lleft_y + target_width)):
    print('Цель поражеена!')

elif (turtle.xcor() >= target_lleft_x and
    turtle.xcor() >= (target_lleft_x + target_width) and
    turtle.ycor() <= (target_lleft_y + target_width) and
    turtle.ycor() <= target_lleft_y):
    print('Мимо!')
    print('Попробуйте угол побольше...')

elif (turtle.xcor() >= (target_lleft_x + target_width) and
    turtle.ycor() <= (target_lleft_y + target_width)):
    print('Мимо!')
    print('Попробуйте угол побольше...')

elif (turtle.xcor() < target_lleft_x  and
    turtle.ycor() < target_lleft_y):
    print('Мимо!')
    print('Попробуйте угол поменьше...')

# не работает, противоречит предыдущему условию
# elif turtle.xcor() < 0:
    # print('Мимо!')
    # print('Попробуйте угол побольше...')

elif (turtle.xcor() < (target_lleft_x + target_width) and
    turtle.ycor() <= (target_lleft_y + target_width) and
    turtle.ycor() <= target_lleft_y):
    print('Мимо!')
    print('Попробуйте скорость побольше...')

elif (turtle.xcor() < target_lleft_x and
    turtle.ycor() >= target_lleft_y):
    print('Мимо!')
    print('Попробуйте угол поменьше...')

elif (turtle.xcor() > (target_lleft_x + target_width) and
    turtle.ycor() > target_lleft_y):
    print('Мимо!')
    print('Попробуйте скорость поменьше...')

elif (turtle.xcor() > target_lleft_x and
    turtle.ycor() > target_lleft_y):
    print('Мимо!')
    print('Попробуйте угол поменьше...')
    print('Попробуйте скорость поменьше...')

turtle.done()