dias = int(input())
km = int(input())

if dias < 0 or km < 0:
    print('Digite a quantidade de dias de locacao:')
    print('Digite a quantidade de km rodados:')
    print('Valor invalido')
else:
    if km > 100:
        valor = (dias * 90) + ((km - (dias*100)) * 12)
        print('Digite a quantidade de dias de locacao:')
        print('Digite a quantidade de km rodados:')
        print('Valor total a ser pago em reais:', valor)
    else:
        valor = (dias * 90)
        print('Digite a quantidade de dias de locacao:')
        print('Digite a quantidade de km rodados:')
        print('Valor total a ser pago em reais:', valor)
