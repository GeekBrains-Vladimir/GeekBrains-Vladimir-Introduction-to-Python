my_list = [23, 423, 45, 235]  # Список изменяемый
for i in range(len(my_list)):
    print(my_list[i])
print(my_list)


my_tuple = tuple(my_list)  # Кортеж - не изменяемый
print(my_tuple)


def func():  # Функция
    a = 5
    b = 6
    c = 7
    return a, b, c


result = func()
# result1, _, result2 = func()
result1, *result2 = func()
print(result)
print(result1)
print(result2)


# Множество. Все элементы уникальны, не упорядоченный список
my_set = set(my_list)
my_set.add(57)
print(my_set)


# Словарь, каждый элемент парный, 1-е значение, ключ - уникальный. Не упорядоченный
my_dict = {4: 'rgg', 6: 'rgg', 'two': 'Двойка',
           (1, 2, 3,): 'Здесь у нас кортеж', True: 'это правда'}
print(my_dict)
print(my_dict[4])
print(my_dict.get(5, 'Ничего нет'))
my_dict[5] = 'Это пятак'
print(my_dict.get(5, 'Ничего нет'))
for i in my_dict:
    print(i)
for i in my_dict.keys():
    print(i)
for i in my_dict.values():
    print(i)
for i in my_dict.items():
    print(i)
for k, v in my_dict.items():
     print(k, v)
