file = open ('Seminar/3Seminar/2Task/text.txt', 'w', encoding='utf-8')
file.write('записать эту строку')
file.close()

file = open ('Seminar/3Seminar/2Task/text.txt', 'r', encoding='utf-8')
data = file.readlines() #read(str) readline(list)
file.close()
print(data)
print(type(data))

file = open ('Seminar/3Seminar/2Task/text.txt', 'a', encoding='utf-8')
file.write('\nДобавили ещё 1 строку')
file.close()

# Чтобы не писать строку с закрыванием файла можно использовать конструкцию:
with open ('Seminar/3Seminar/2Task/text.txt', 'a', encoding='utf-8') as data:
    data.write('\nsdfsfsg')
    data.write('1234564')