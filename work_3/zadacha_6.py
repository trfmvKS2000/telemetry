def fun(a):
    return a.title()
print(fun("kseniya"))

def fun1(a):
    x = a.split(' ')
    k = []
    for i in x:
        el = str(i)
        x = el[:1].upper()
        z = x + el[1:]
        k.append(z)
    return k
print(fun1("trofimova kseniya denisovna"))