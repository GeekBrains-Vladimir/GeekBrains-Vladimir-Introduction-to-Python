# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

Numbers = []
for i in range(5):
    Numbers.append(int(input(f'Введите {i+1}-е число: ')))
MyMax = Numbers[0]
# for i in range(len(Numbers)):
#     if Numbers[i] > MyMax:
#         MyMax = Numbers[i]
for item in Numbers:
    if MyMax < item:
        MyMax = item
print(f'Наибольшее число равно: {MyMax}')
