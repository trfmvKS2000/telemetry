with open("#4_5.txt", 'w') as file:
    str = ['19 18 27 1']
    file.writelines(str)
with open('#4_5.txt', 'r') as file:
    numbers_str = file.read()
    numbers_lst = numbers_str.split(' ')
    print(f"Числа:\n{numbers_str}")
    print(f"Сумма чисел:\n{sum([int(i) for i in numbers_lst])}")