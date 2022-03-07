e3a4i1s5 = 'abc'
while e3a4i1s5 != '541r' or e3a4i1s5 != 'f1m':
    palavra = input()
    palavra = palavra.replace('3', 'e')
    palavra = palavra.replace('4', 'a')
    palavra = palavra.replace('1', 'i')
    palavra = palavra.replace('5', 's')
    e3a4i1s5 = palavra.upper()

    if e3a4i1s5 == 'FIM' or e3a4i1s5 == 'SAIR':
        break

    else:
        print(e3a4i1s5)
