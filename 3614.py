qtd_criancas = int(input())
sexo = ''
t_vida = 0
meninos = 0
meninas = 0
i = 0
t_vida_24_menos = 0

if qtd_criancas <= 0:
    print('Informe um n�mero positivo')
else:
    while i < qtd_criancas:
        sexo = input()
        t_vida = int(input())
        if sexo == 'M':
            meninos += 1
        elif sexo == 'F':
            meninas += 1
        else:
            print('Inv�lido')
        if t_vida <= 24:
            t_vida_24_menos += 1
        i += 1
    print(f'a) {meninas/qtd_criancas*100}% das crian�as eram do sexo feminino.')
    print(f'b) {meninos/qtd_criancas*100}% das crian�as eram do sexo masculino.')
    print(
        f'c) {t_vida_24_menos/qtd_criancas*100}% das crian�as viveram 24 meses ou menos.')
