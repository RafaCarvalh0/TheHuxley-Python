name = input()
name = name.split()
name2 = []
lista = ['e', 'da', 'de', 'di', 'do', 'du']
exit = ['*']
while name != exit:
    for connectives in name:
        connectives = connectives.lower()
        if connectives not in lista:
            new_connectives = connectives.title()
            name2.append(new_connectives)
        else:
            name2.append(connectives)
        nome3 = ' '.join(name2)
    print(nome3)
    name2.clear()
    name = input().split()
