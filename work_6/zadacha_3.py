import math
import matplotlib.pyplot as plt
import numpy as np

def devizion(a,b,c):
    try:
        D = (b ** 2) - 4 * a * c
        x1 = (-b + math.sqrt(D)) / 2 * a
        x2 = (-b - math.sqrt(D)) / 2 * a
    except TypeError:
        D = f'{a},{b},{c} Переменная должна быть числом'
    except UnboundLocalError:
        x1 = 'Корня нет'
        x2 = 'Корня нет'
    except ValueError:
        x1 = 'Корня нет'
        x2 = 'Корня нет'

    return D, x1, x2

print (devizion(int(input("Введите первое число а:")), int(input("Введите второе число b: ")), int(input("Введите третье число c:"))))


a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третье число:'))
x = np.linspace(-100,100, 100)
y = a*x**2 + b*x + c
fig, ax = plt.subplots()
ax.plot(x, y, color="green", label="y(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

plt.show()