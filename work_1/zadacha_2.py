sec=int(input('Введите число:'))
chas = sec // 3600
ost = sec % 3600
min = sec // 60
sec1 = ost % 60

print(f'Перевод выполнен:{sec}:{min}:{chas}')