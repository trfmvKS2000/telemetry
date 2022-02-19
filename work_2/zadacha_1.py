x1 = 8
Z = 1.4
str = "Строка"
list = ['a', '2']
tuple = ('b', '3')
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
massive = [1, 2, 3, 4, 5, 'today', False]

vivod = [x1, Z, str, list, tuple, set1, massive]
for i in vivod:
    print(f'{i} is {type(i)}')