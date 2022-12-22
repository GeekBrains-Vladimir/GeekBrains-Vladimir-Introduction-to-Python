
print("\033c")
print('Программа на вход принимает значение N и выводит на экран значения от -N до N')
print(" ")
number = int(input('Введите число N: '))
my_list = []
# for i in range(-number, number+1):
#     if i == number:
#         print(i)
#     else:
#         print(i, end = ', ')
for i in range(-number, number+abs(number)//number, abs(number)//number):
    my_list.append(i)    
print(*my_list, sep = ', ')
