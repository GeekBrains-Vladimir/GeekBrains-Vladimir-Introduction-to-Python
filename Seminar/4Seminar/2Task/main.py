my_string = '   Питон самый лучший язык в мире\n'
# my_string = my_string.split('и') #split - разделяет и удаляет символ
# my_string = my_string.replace('и', '$') # replace - замена символа
# my_string = my_string.startswith('Пит')
print(my_string)
print(my_string.lower().startswith('пит'))
print(my_string.upper().startswith('ПИТ'))
print(my_string.strip())

my_list = ['1', '2', '3', '4', '5', '6']
glue = '-z-'
print(' '.join(my_list))
print(glue.join(my_list))
