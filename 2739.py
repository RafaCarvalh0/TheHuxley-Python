info = input().split()
raca = info[0]
hora = info[1]
tempo = info[2]
altura = float(info[3])
luta = float(info[4])
stealth = float(info[5])

#-----------------AN?O----------------#
if raca == 'A':
    if altura > 1.80:
        stealth = stealth - 5
    elif altura < 1.50:
        stealth = stealth + 2
    chance_anao = ((luta + stealth) / 2) * 10
    if chance_anao > 100:
        chance_anao = 100.00
        print(
            f'A taxa de sucesso do anao para entrar em Novigrad e de {chance_anao:.2f}%')
    elif chance_anao < 0:
        chance_anao = 0.00
        print(
            f'A taxa de sucesso do anao para entrar em Novigrad e de {chance_anao:.2f}%')
    else:
        print(
            f'A taxa de sucesso do anao para entrar em Novigrad e de {chance_anao:.2f}%')

#-----------------BRUXO----------------#
elif raca == 'B':
    if hora == 'D':
        chance_bruxo = 0.00
    elif tempo == 'n':
        chance_bruxo = 100.00
    else:
        if tempo == 'c':
            luta = luta + 3
            stealth = stealth + 3
        if tempo == 's':
            stealth = stealth - 1
        if altura < 1.70:
            stealth = stealth + 3
        elif altura > 2.00:
            stealth = stealth - 4
        chance_bruxo = ((luta + stealth) / 2) * 10
    if chance_bruxo > 100:
        chance_bruxo = 100.00
        print(
            f'A taxa de sucesso do bruxo para entrar em Novigrad e de {chance_bruxo:.2f}%')
    elif chance_bruxo < 0:
        chance_bruxo = 0.00
        print(
            f'A taxa de sucesso do bruxo para entrar em Novigrad e de {chance_bruxo:.2f}%')
    else:
        print(
            f'A taxa de sucesso do bruxo para entrar em Novigrad e de {chance_bruxo:.2f}%')

#-----------------ELFO----------------#
elif raca == 'E':
    if hora == 'N':
        chance_elfo = 0.00
    elif tempo == 'n':
        chance_elfo = 0.00
    else:
        if tempo == 'c':
            luta = luta - 2
        elif tempo == 's':
            stealth = stealth - 1
        if altura < 1.60:
            stealth = stealth + 1
        elif altura > 1.90:
            stealth = stealth - 6
        chance_elfo = ((luta + stealth) / 2) * 10
    if chance_elfo > 100:
        chance_elfo = 100.00
        print(
            f'A taxa de sucesso do elfo para entrar em Novigrad e de {chance_elfo:.2f}%')
    elif chance_elfo < 0:
        chance_elfo = 0.00
        print(
            f'A taxa de sucesso do elfo para entrar em Novigrad e de {chance_elfo:.2f}%')
    else:
        print(
            f'A taxa de sucesso do elfo para entrar em Novigrad e de {chance_elfo:.2f}%')

#-----------------HUMANO----------------#
elif raca == 'H':
    chance_humano = 100.00
    print(
        f'A taxa de sucesso do humano para entrar em Novigrad e de {chance_humano:.2f}%')
