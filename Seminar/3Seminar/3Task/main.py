# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
my_list = ['123', 'dsf', 'sdf', '43.5', 'dfta', 'djf']
search = 'df'
a = 0
for i in range(len(my_list)):
    if search in my_list[i]: # == полное совпадение, in находит вхождение в подстроку
        print(f'Элемент {search} найден в элементе {my_list[i]}')
        a = 1

    # if my_list[i].find(str(search)) != -1:
    #     print(f'Элемент {search} найден в элементе {my_list[i]}')
    # a = 1
if a == 0:
    print('Такого элемента нет')
