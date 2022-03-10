with open("#4_2.txt", 'w') as file_obj:
    file = ['last name first name\n', 'phone number\n', 'date of birth\n', 'place of residence\n', 'place of work / study\n', 'additional information\n']
    file_obj.writelines(file)
with open("#4_2.txt") as file_obj:
    stroki = 0
    simvoli = 0
    for line in file_obj:
        stroki += line.count("\n")
        simvoli = len(line)-1
        print(f"{simvoli} символов в строке")
    print(f"Всего строк: {stroki}")