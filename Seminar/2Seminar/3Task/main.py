print("\033c")
print('Программа на вход принимает дробь и выводит первую цифру дробной части')
print(" ")
Num = float(input('Введите вещественное число N: '))
if (int(Num) == Num):
    print(f'У числа {int(Num)} нет дробной части')
else:
    A = int(abs(Num)*10) % 10
    print(f' Первая цифра дробной части числа {Num} -> {A}')

# Num = input('Введите вещественное число: ')
# Num = Num.split('.')
# if len(Num) > 1:
#     print(Num[1][0])
# else:
#     print('Число целое')
