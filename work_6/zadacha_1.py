def devizion(number_1, number_2):
    result = 0
    try:
        result = number_1+number_2
    except TypeError:
        result = f'{number_1} или {number_2}' 'Переменная должна быть числом'
    return result

print(devizion(5, 5))
print(devizion(19, -18))
print(devizion('О', 0))
print(devizion('Hi', 7))