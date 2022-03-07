valor = int(input())
print('Digite o pH da solucao:')

if valor > 0 and valor < 7:
    print('Essa solucao e acida.')
elif valor > 7 and valor <= 14:
    print('Essa solucao e basica.')
elif valor == 7:
    print('Essa solucao e neutra.')
else:
    print('Valor deve estar entre 0 e 14.')
