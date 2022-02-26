def fun(a, b, c):
    suma = [a, b, c]
    sp = [ ]

    a = max(suma)
    sp.append(a)
    suma.remove(a)
    b = max(suma)
    sp.append(b)
    print(sum(sp))
print(fun(int(input("Введите первое число:")), int(input("Введите второе число: ")), int(input("Введите третье число:"))))