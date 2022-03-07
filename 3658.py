x = input()
x = x.split(',')
lista_de_itens = [5.50, 6.00, 7.50, 1.99, 4.00, 6.70, 1.20, 2.80, 5.30, 5.00, 3.00, 2.00,
                  3.50, 0.80, 1.00, 0.80, 5.40, 1.90, 5.00, 10.00, 0.50, 0.50, 5.00, 4.50, 1.99, 2.90, 0.30]
sum = 0
i = 0
while i < len(x):
    sum = sum + int(x[i]) * lista_de_itens[i]
    i += 1

valor_doado = int(input())
qtd_cestas = valor_doado / sum
print(f'O valor da cesta b�sica ficou em: R${sum:.2f}')
print('Com o valor doado pode ser comprada', int(qtd_cestas), 'cestas b�sicas')
