# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
print("\033c")
import random
text = []
for i in range(10):
    index = random.randint(0, 2)
    text.append(round(random.uniform(0, 10), index))
print(f'Наш список: \n{text}')
Max = round(text[0] % 1, 2)
for i in range(len(text)):
    if text[i] % 1 != 0:
        Min = round(text[i] % 1, 2)
        break
for i in range(len(text)):
    if text[i] % 1 > Max:
        Max = round(text[i] % 1, 2)
    elif text[i] % 1 < Min and text[i] % 1 != 0:
        Min = round(text[i] % 1, 2)
result = round((Max-Min), 2)
print(f'Максимальное значение равно {Max}, минимальное значение равно {Min}, разница равна: {result}')