entrada = input()
entrada = entrada.split()
colunas = int(entrada[0])
linhas = int(entrada[1])
i = 0
for i in range(3):
    blue = list()
    red = list()
    green = list()
    coluna_escolhida = int(input())
    cor_escolhida = input().upper()
# AZUL=============================================================
    if cor_escolhida == 'B':
        print('')
        while coluna_escolhida <= (colunas * linhas):
            if coluna_escolhida > (colunas * linhas):
                break
            if (coluna_escolhida % 2) == 1:
                blue.append(coluna_escolhida)
            coluna_escolhida = (coluna_escolhida + colunas)
        for numeros_luzes in blue:
            print(numeros_luzes)
# VERMELHO========================================================
    elif cor_escolhida == 'R':
        print('')
        while coluna_escolhida <= (colunas * linhas):
            red.append(coluna_escolhida)
            coluna_escolhida = (coluna_escolhida + colunas)
            if coluna_escolhida > (colunas * linhas):
                break
        for numeros_luzes in red:
            print(numeros_luzes)
# VERDE==========================================================
    elif cor_escolhida == 'G':
        print('')
        while coluna_escolhida <= (colunas * linhas):
            if coluna_escolhida > (colunas * linhas):
                break
            if (coluna_escolhida % 2) == 0:
                green.append(coluna_escolhida)
            coluna_escolhida = (coluna_escolhida + colunas)
        for numeros_luzes in green:
            print(numeros_luzes)
    i = i + 1
