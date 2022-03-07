chegada = {}
mesa = [0 for i in range(5)]
pos = 1
chegada[input()] = pos
pos += 1
chegada[input()] = pos
pos += 1
chegada[input()] = pos
pos += 1
chegada[input()] = pos
pos += 1
chegada[input()] = pos
mesa[0] = 'Princesa'

if not (chegada['Mario'] % 2):
    mesa[1] = 'Mario'
else:
    mesa[2] = 'Mario'

if not (chegada['Toad'] % 2):
    if mesa[1]:
        mesa[3] = 'Toad'
    else:
        mesa[1] = 'Toad'
else:
    if mesa[2]:
        mesa[4] = 'Toad'
    else:
        mesa[2] = 'Toad'

if not (chegada['Luigi'] % 2):
    if mesa[1]:
        mesa[3] = 'Luigi'
    else:
        mesa[1] = 'Luigi'
else:
    if mesa[2]:
        mesa[4] = 'Luigi'
    else:
        mesa[2] = 'Luigi'


if not (chegada['Yoshi'] % 2):
    if mesa[1]:
        mesa[3] = 'Yoshi'
    else:
        mesa[1] = 'Yoshi'
else:
    if mesa[2]:
        mesa[4] = 'Yoshi'
    else:
        mesa[2] = 'Yoshi'

for i in mesa:
    print(i)
