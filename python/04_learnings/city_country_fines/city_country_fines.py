print("Система расчета штрафов")

car_speed = 51
is_town = True
is_camera = False

fine_for_01_to_10 = 30
fine_for_11_to_15 = 50
fine_for_16_to_20 = 70
fine_for_21_to_25 = 115
fine_for_26_to_30 = 180
fine_for_31_to_40 = 260
fine_for_41_to_50 = 400
fine_for_51_to_60 = 560
fine_for_61_to_70 = 700
fine_for_70_and_more = 800

town_speed = 50
country_speed = 70

if is_town:
 over_speed = car_speed - town_speed
else:
 over_speed = car_speed - country_speed

if is_camera and over_speed > 60:
  print("Лишение водительских прав")


if over_speed < 1:
 print("Скорость не превышена или превышена незначительно")
elif over_speed >= 1 and over_speed <= 10:
 print("Штраф: " + str(fine_for_01_to_10) + " euro")
elif over_speed >= 11 and over_speed <= 15:
 print("Штраф: " + str(fine_for_11_to_15) + " euro")
elif over_speed >= 16 and over_speed <= 20:
 print("Штраф: " + str(fine_for_16_to_20) + " euro")
elif over_speed >= 21 and over_speed <= 25:
 print("Штраф: " + str(fine_for_21_to_25) + " euro")
elif over_speed >= 26 and over_speed <= 30:
 print("Штраф: " + str(fine_for_26_to_30) + " euro")
elif over_speed >= 31 and over_speed <= 40:
 print("Штраф: " + str(fine_for_31_to_40) + " euro")
elif over_speed >= 41 and over_speed <= 50:
 print("Штраф: " + str(fine_for_41_to_50) + " euro")
elif over_speed >= 51 and over_speed <= 60:
 print("Штраф: " + str(fine_for_51_to_60) + " euro")
elif over_speed >= 61 and over_speed <= 70:
 print("Штраф: " + str(fine_for_61_to_70) + " euro")
elif over_speed >= 70:
 print("Штраф: " + str(fine_for_70_and_more) + " euro")