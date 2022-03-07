primeira_frase = input()
primeira_ordem = []
segunda_frase = input()
segunda_ordem = []
for caracter in primeira_frase:
    if caracter not in " .,!?":
        primeira_ordem.append(caracter.upper())
primeira_ordem.sort()

for caracter in segunda_frase:
    if caracter not in " .,!?":
        segunda_ordem.append(caracter.upper())
segunda_ordem.sort()

if primeira_ordem == segunda_ordem:
    print('True')
else:
    print('False')
