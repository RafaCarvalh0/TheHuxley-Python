i = 0
mesa1 = list()
mesa2 = list()
mesa3 = list()
mesa4 = list()
nit = input().lower()  # NIT = NOME + IDADE + TIME

while nit != '-1':

    nit = nit.split()
    nome = nit[0].upper()
    idade = int(nit[1])
    time = nit[2]
    if (time == 'sport' or time == 'vitoria' or time == 'flamengo') and idade >= 30:
        mesa1.append(nome)
    elif (time == 'treze' or time == 'santos' or time == 'vasco') and idade >= 18 and idade <= 36:
        mesa2.append(nome)
    elif (time == 'bahia' or time == 'fortaleza' or time == 'gremio') and idade > 10 and idade < 18:
        mesa3.append(nome)
    else:
        mesa4.append(nome)
    i = i + 1
    if i == 10:
        break
    nit = input().lower()


if i != 0:
    # MESA 1 -------------------------------
    print('MESA 1')
    if len(mesa1) != 0:
        i = 0
        while i < len(mesa1):
            print(i+1, mesa1[i])
            i = i + 1
    elif len(mesa1) == 0:
        print('VAZIA')
# MESA 2 -------------------------------
    print('\nMESA 2')
    if len(mesa2) != 0:
        i = 0
        while i < len(mesa2):
            print(i + 1, mesa2[i])
            i = i + 1
    elif len(mesa2) == 0:
        print('VAZIA')
# MESA 3 -------------------------------
    print('\nMESA 3')
    if len(mesa3) != 0:
        i = 0
        while i < len(mesa3):
            print(i + 1, mesa3[i])
            i = i + 1
    elif len(mesa3) == 0:
        print('VAZIA')
# MESA 4 -------------------------------
    print('\nMESA 4')
    if len(mesa4) != 0:
        i = 0
        while i < len(mesa4):
            print(i + 1, mesa4[i])
            i = i + 1
    elif len(mesa4) == 0:
        print('VAZIA')
# JANTAR SEM CONVIDADOS---------------
elif i == 0:
    print('JANTAR SEM CONVIDADOS')
