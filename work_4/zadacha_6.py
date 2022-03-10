import re

sp = {}
with open('#4_6.txt', 'r') as file:
    text = file.read()
    file.seek(0)

    for i in file:
        i_items = i.split(': ')
        chas = re.findall(r"\d+", i_items[1])
        sp.update({i_items[0]: sum([int(i) for i in chas])})

print(f"Словарь:\n{sp}")