# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве 
# (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти растояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
import math
ax = int(input('Введите координату X точки a: '))
ay = int(input('Введите координату Y точки a: '))
bx = int(input('Введите координату X точки b: '))
by = int(input('Введите координату Y точки b: '))
distance = round(math.sqrt(((ax-bx)**2) + ((ay-by)**2)),2)
print(f'Расстояние между точкой а ({ax},{ay} и точкой b ({bx},{by}) = {distance}')

