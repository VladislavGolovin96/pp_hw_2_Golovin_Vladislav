
import math

#Домашнее задание №2
#Вычислить длину соответствующей окружности для круга и его площадь
while True:
    try:
        radius: float = float(input("Введите значение радиуса в см.: "))
        circumference_length: float = math.pi * (radius * 2)
        circle_area: float  = math.pi * pow(radius, 2)
        print(f"Длина окружности равна: {round(circumference_length, 2)} см.\nПлощадь круга равна: {round(circle_area, 2)} см.")
    except ValueError:
        print("Системная ошибка, введите корректные данные!")