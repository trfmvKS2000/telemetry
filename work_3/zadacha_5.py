res = 0
while True:
    sp = input("Введите число: ")
    z = sp.split(" ")
    for i in z:
        try:
            x = float(i)
            res += x
        except:
            if i == 'STOP':
                print(f"Сумма: {res}")
                exit(0)
            else:
                print(f"Сумма: {res}")
                exit(1)