nota = float(input())  # informe a nota
qtd_listas = int(input())  # informe a quantidade de listas
listas = []

for i in range(qtd_listas):
    lista = float(input())  # informe a nota da lista 1,2,3...
    if 0 <= lista <= 10:
        listas.append(lista)

nota_final = (nota * 0.70) + ((sum(listas) / qtd_listas) * 0.30)

if 0 <= nota_final < 3:
    print(f'{nota_final:.2f}')
    print('RED ZONE!')
if 3 <= nota_final < 5:
    print(f'{nota_final:.2f}')
    print('DA PARA RECUPERAR!')
if 5 <= nota_final < 7:
    print(f'{nota_final:.2f}')
    print('QUASE LA!')
if 7 <= nota_final < 9:
    print(f'{nota_final:.2f}')
    print('TA FAVORAVEL!')
if nota_final >= 9:
    print(f'{nota_final:.2f}')
    print('EXCELENTE!')
