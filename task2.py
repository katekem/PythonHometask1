# Напишите программу для проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x or y or y) == (not x and not y and not z):
                print(f'x = {x}, y = {y}, z = {z} | True')
            else:
                print(f'x = {x}, y = {y}, z = {z} | False')

