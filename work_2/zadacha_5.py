N = int(input("Введите число: "))
list = [11, 7, 5, 3, 3, 2]
x = list.count(N)
for element in list:
    if x > 0:
        z = list.index(N)
        list.insert(z+x, N)
        break
    else:
        if N > element:
            y = list.index(element)
            list.insert(y, N)
            break
        elif N < list[len(list) - 1]:
            list.append(N)

print(list)