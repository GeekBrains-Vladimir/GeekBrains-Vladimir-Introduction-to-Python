# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print("\033c")
print('Программа для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')
print('')
for x in (True, False):
    for y in (True, False):
        for z in (True, False):
            if not (x or y or z) == (not x and not y and not z):
                print(f'Выражение верно при значении x={x}, y={y}, y={z}')
