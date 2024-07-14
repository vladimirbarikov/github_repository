# эта программа наносит звезды Ориона
# названия звезд и линии созвездия

import turtle

# задать размер окна
turtle.setup(500, 600)
turtle.speed(2)

# поднять перо черепахи
turtle.penup()

# создать именованные константы для звездных координат
left_shoulder_x = -70
left_shoulder_y = 200

right_shoulder_x = 80
right_shoulder_y = 180

left_beltstar_x = -40
left_beltstar_y = -20

middle_beltstar_x = 0
middle_beltstar_y = 0

right_beltstar_x = 40
right_beltstar_y = 20

left_knee_x = -90
left_knee_y = -180

right_knee_x = 120
right_knee_y = -140

# нанести звезды
turtle.goto(left_shoulder_x, left_shoulder_y)  # левое плече
turtle.dot()
turtle.goto(right_shoulder_x, right_shoulder_y)  # правое плече
turtle.dot()
turtle.goto(left_beltstar_x, left_beltstar_y)  # левая звезда в поясе
turtle.dot()
turtle.goto(middle_beltstar_x, middle_beltstar_y)  # средняя звезда в поясе
turtle.dot()
turtle.goto(right_beltstar_x, right_beltstar_y)  # правая звезда в поясе
turtle.dot()
turtle.goto(left_knee_x, left_knee_y)  # левое колено
turtle.dot()
turtle.goto(right_knee_x, right_knee_y)  # правое колено
turtle.dot()

# вывести названия звезд
turtle.goto(left_shoulder_x, left_shoulder_y)  # Бетельгейзе
turtle.write('Бетельгейзе')
turtle.goto(right_shoulder_x, right_shoulder_y)  # Хатиса
turtle.write('Хатиса')
turtle.goto(left_beltstar_x, left_beltstar_y)  # Альнитак
turtle.write('Альнитак')
turtle.goto(middle_beltstar_x, middle_beltstar_y)  # Альнилам
turtle.write('Альнилам')
turtle.goto(right_beltstar_x, right_beltstar_y)  # Минтака
turtle.write('Минтака')
turtle.goto(left_knee_x, left_knee_y)  # Саиф
turtle.write('Саиф')
turtle.goto(right_knee_x, right_knee_y)  # Ригель
turtle.write('Ригель')

# нанести линию из левого плеча в левую звезду пояса
turtle.goto(left_shoulder_x, left_shoulder_y)
turtle.pendown()
turtle.goto(left_beltstar_x, left_beltstar_y)
turtle.penup()

# нанести линию из правого плеча в правую звезду пояса
turtle.goto(right_shoulder_x, right_shoulder_y)
turtle.pendown()
turtle.goto(right_beltstar_x, right_beltstar_y)
turtle.penup()

# нанести линию из левой звезды в среднюю звезду пояса
turtle.goto(left_beltstar_x, left_beltstar_y)
turtle.pendown()
turtle.goto(middle_beltstar_x, middle_beltstar_y)
turtle.penup()

# нанести линию из средней звезды в правую звезду пояса
turtle.goto(middle_beltstar_x, middle_beltstar_y)
turtle.pendown()
turtle.goto(right_beltstar_x, right_beltstar_y)
turtle.penup()

# нанести линию из левой звезды в левое колено
turtle.goto(left_beltstar_x, left_beltstar_y)
turtle.pendown()
turtle.goto(left_knee_x, left_knee_y)
turtle.penup()

# нанести линию из правой звезды в правое колено
turtle.goto(right_beltstar_x, right_beltstar_y)
turtle.pendown()
turtle.goto(right_knee_x, right_knee_y)
turtle.penup()

turtle.done()