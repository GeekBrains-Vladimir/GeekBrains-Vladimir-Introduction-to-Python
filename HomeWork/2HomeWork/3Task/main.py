# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int
print("\033c")
print('Алгоритм перемешивания списка')
print('')
N = int(input('Дружище, введи длину списка: '))
print('')
from random import randrange
from random import randint
Mass = []
for i in range (N):
    X = randint(-10,10)
    Mass.append(X)
print(f'Список: \t \t {Mass}')
for i in range(N):
    N1, N2 = randrange(N), randrange(N)
    Mass[N1], Mass[N2] = Mass[N2], Mass[N1]
print(f'Перемешанный список: \t {Mass}')





# Sum = 0
# for i in range(1, N+1):
#     Funk = round((1+1/i)**i, 2)
#     Sum += Funk
#     Reload.append(Funk)
# print(f'Последовательность: {Reload}')
# print(f'Сумма всех значений равна: {Sum}')