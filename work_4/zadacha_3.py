file = {'Trofimova': 10, 'Smirnov': 10, 'Popov': 7, 'Ivanov': 8, 'Antonova': 5, 'Shevelev': 6, 'Postov': 4}
try:
    file_obj = open("#4_3.txt", 'w')
    for familia, stipendia in file.items():
        file_obj.write(familia + ':' + str(stipendia) + "\n")
except IOError:
    print("Ошибка")
finally:
    file_obj.close()
summa = 0
stip = 0
fam = []
with open("#4_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 5:
            fam.append(tokens[0])
        summa += int(tokens[1])
        stip += 1
    srednee = summa / stip
    print(f"Фамилии: {fam}")
    print(f"Среднее: {srednee}")