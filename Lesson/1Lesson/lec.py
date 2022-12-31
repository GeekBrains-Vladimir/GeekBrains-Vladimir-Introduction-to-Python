# # print('hello word')
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# value = None
# # print(type(value))
# value = 12334
# # print(type(value))
# s = "' qwerty \n hello \'word'"
# print(s) # вывод строки
# print (a, ' - ', b, ' - ', s)
# print ('{1} - {2} - {0}'. format (a, b, s))
# print (f'{a} - {b} - {s}')

# f = False
# print(f)

# list = ['1', '2', '3', 'hello', 1,2,3, 4.5, True]
# print(list)

# # Ввод и вывод данных
# # print, input

# print('Введите а')
# a = int (input()) # float
# print('Введите в')
# b = int (input()) # float
# print(a, '+', b, '=', a+b)


# Арифметические операции
# Важно и нужно, без них вы не напишете ни одной
# программы
# Если помните математику – проблем не будет
# +, -, *, /, %, //, **
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# ( ) Скобки меняют приоритет

# a = 1.312312
# b = 3
# c = round(a*b, 7)
# print(c)

# a = 3
# a =+ 5
# print (a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# a = 1 != 2
# print(a)

# a= 'qwerty'
# b = 'qwerty'
# print (a == b)
# a = 1 < 3 < 5 < 10
# print(a)
# func = 1
# T = 4
# X = 123
# print(func<T>X)
# f = 1 > 2 or 4 < 6
# print(f)
# f = [1,2,3,4]
# print(f)
# print(not 2 in f)
# is_odd = not f[0] % 2
# print(is_odd)


# Управляющие конструкции: if, if-else
# Условный оператор позволяет управлять ходом
# выполнения программы
# if condition:
#     # operator 1
#     # operator 2
#     # ...
#     # operator n
# else:
#     # operator n + 1
#     # operator n + 2
#     # ...
#     # operator n + m

# a = int(input('a = '))
# b = int(input('b = '))

# # if condition1:
#     # operator
# elif condition2:
#     # operator
# elif condition3:
#     # operator
# else:
#     # operator

# username = input ('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print ('Я так ждала Вас, Марина!')
# elif username == 'Ильнаро':
#     print('Ильгар - ТОПчик')
# else:
#     print('Привет,', username)

# Управляющие конструкции: while
# while condition:
#     # operator 1
#     # operator 2
#     # . . .
#     # operator n
# Цикл позволяет выполнить блок операторов какое-
# то количество раз

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# Управляющие конструкции: while-else
# while condition:
#     # operator 1
#     # operator 2
#     # . . .
#     # operator n
# else:
#     # operator n + 1
#     # operator n + 2
#     # . . .
#     # operator n + m
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Управляющие конструкции: for
# for i in enumeration:
#     # operator 1
#     # operator 2
#     # . . .
#     # operator n
# Когда мы знаем, что хотим

# r = range(10)
# for i in r:
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in 'q-w-rt - y':
#      print(i)

# Немного о строках
# text = 'съешь ещё этих мягких французских булок'
# print(len(text))       # 39
# print('ещё' in text)   # True
# print(text.isdigit())  # False
# print(text.islower())  # True
# print(text.replace('ещё','ЕЩЁ'))  #
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])   # c
# print(text[1])   # ъ
# print(text[len(text)-1])  # к
# print(text[-5])  # б
# print(text[:])   # print(text)
# print(text[:2])  # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # сеикакл
# print(text[::6])  # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# ran = range(1,6)
# numbers = list(ran)
# print(type(ran))
# print(numbers)  # [1, 2, 3, 4, 5]
# print(type(numbers))
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)    # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)   # red green blue
# for e in colors:
#     print(e*2)   # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# Функции
# Это фрагмент программы, используемый 
# многократно
# def function_name(x):
# # body line 1
# # . . .
# # body line n
#     # optional return 

def f(x):
    return x**2
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 2.3
print(f(arg))
print(type(f(arg)))