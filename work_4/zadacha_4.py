sp = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

angl = ''
with open('#4_4.txt', 'r') as file_angl:
    angl = file_angl.read()
rus = angl
for en, ru in sp.items():
    rus = rus.replace(en, ru)
with open('#4_4new.txt', 'w') as file_rus:
    file_rus.write(rus)