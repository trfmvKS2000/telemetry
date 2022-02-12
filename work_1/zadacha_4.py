y = input("Введите целое положительное число: ")
x = 0
for i in y:
    while int(i) > x:
        x = int(i)
print(f'Итог:{x}')