def fun (a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        print("Введите второе число правильно")

print(fun(int(input("Введите первое число:")), int(input("Введите второе число: "))))
