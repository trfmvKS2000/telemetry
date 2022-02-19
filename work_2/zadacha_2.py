sp = []
n=int(input('Введите количество значений'))
for i in range(n):
    sp.append(int(input('Введите значение')))

if len(sp) % 2 == 0:
    i = 0

    while i < len(sp):
        x = sp[i]
        sp[i] = sp[i+1]
        sp[i+1] = x
        i += 2

else:
    i = 0
    while i < len(sp) - 1:
        x = sp[i]
        sp[i] = sp[i+1]
        sp[i+1] = x
        i += 2

print(sp)