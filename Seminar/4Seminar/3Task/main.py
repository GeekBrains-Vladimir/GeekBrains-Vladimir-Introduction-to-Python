# Найдите корни квадратного уравнения Ax² + Bx + C = 0 с помощью математических формул нахождения корней квадратного уравнения
import math
equation = '3*x**2 + 5*x - 6 = 0'


def create_koef(equation: str):
    new_equation = equation.replace(' ', '').replace(
        '=0', '').replace('+', ' ').replace('-', ' -')
    new_equation = new_equation.split()
    new_list = []
    for i in new_equation:
        if i.startswith('x'):
            new_list.append(1)
        elif i.startswith('-x'):
            new_list.append(-1)
        else:
            new_list.append(i.split('*x')[0])
    return new_list


def solve_equation(koef):
    a, b, c = int(koef[0]), int(koef[1]), int(koef[2])
    disc = b**2-4*a*c
    if disc > 0:
        x1 = (-b-math.sqrt(disc))/(2*a)
        x2 = (-b+math.sqrt(disc))/(2*a)
        return round(x1, 2), round(x2, 2)
    elif disc == 0:
        x = (-b-math.sqrt(disc))/(2*a)
        return round(x, 2)
    else:
        return None
print(create_koef(equation))
print(solve_equation(create_koef(equation)))

# my_list = equation.replace('*x**2', '')
# my_list = my_list.replace('*x', '')
# # my_list = my_list.replace(' = 0', '')
# my_list = my_list.split(' ')
# A = int(my_list[0])
# B = int(my_list[2])
# C = int(my_list[4])
# if my_list[1] == '-':
#     B *= -1
# if my_list[3] == '-':
#     C *= -1
# discriminant = B**2 - 4*A*C

# if discriminant < 0:
#     print('решений нет')
# elif discriminant == 0:
#     print(-(B/(2*A)))
# else:
#     X1 = round((-B+(discriminant)**0.5)/(2*A), 3)
#     X2 = round((-B-(discriminant)**0.5)/(2*A), 3)
# print(my_list)
# print(f'A = {A}, B = {B}, C = {C}')
# print(f'X1 = {X1}, X2 = {X2}')
