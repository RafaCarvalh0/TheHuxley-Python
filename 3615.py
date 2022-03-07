nome = [input()]
veiculos = [int(input())]
fatal = [int(input())]
nao_fatal = [int(input())]
sem_vitimas = [int(input())]

i = 0
totalveiculos = 0
total_de_acidentes = 0
totalfatal = 0
total_de_acidentes_nao_fatais = 0
totalvict = 0
totalsem_vitimas = 0
mais_acidentes = 0
menos_acidentes = 9999999999
IND = []
IVTH = 0
IVTL = 9999999

outro_municipio = input()

IVT = (5 * fatal[i] + 3 * nao_fatal[i] + sem_vitimas[i]) / veiculos[i]
IND.append(IVT)
total_de_acidentes += fatal[i] + nao_fatal[i] + sem_vitimas[i]
total_de_acidentes1 = fatal[i] + nao_fatal[i] + sem_vitimas[i]
totalveiculos += veiculos[i]
totalvict += fatal[i] + nao_fatal[i]

if total_de_acidentes >= mais_acidentes:
    mais_acidentes = total_de_acidentes
    MAIS = i
if total_de_acidentes <= menos_acidentes:
    menos_acidentes = total_de_acidentes
    MENOS = i
if IVT >= IVTH:
    IVTH = IVT
    H = i
if IVT <= IVTL:
    IVTL = IVT
    L = i
totalfatal += fatal[i]
total_de_acidentes_nao_fatais += nao_fatal[i]
totalsem_vitimas += sem_vitimas[i]
i += 1

while outro_municipio == 'S':

    nome.append(input())
    veiculos.append(int(input()))
    fatal.append(int(input()))
    nao_fatal.append(int(input()))
    sem_vitimas.append(int(input()))
    outro_municipio = input()

    IVT = (5 * fatal[i] + 3 * nao_fatal[i] + sem_vitimas[i]) / veiculos[i]
    IND.append(IVT)
    total_de_acidentes += fatal[i] + nao_fatal[i] + sem_vitimas[i]
    total_de_acidentes1 = fatal[i] + nao_fatal[i] + sem_vitimas[i]
    totalveiculos += veiculos[i]
    totalvict += fatal[i] + nao_fatal[i]
    totalfatal += fatal[i]

    if total_de_acidentes1 >= mais_acidentes:
        mais_acidentes = total_de_acidentes1
        MAIS = i
    if total_de_acidentes1 <= menos_acidentes:
        menos_acidentes = total_de_acidentes1
        MENOS = i
    if IVT > IVTH:
        IVTH = IVT
        H = i
    if IVT < IVTL:
        IVTL = IVT
        L = i
    total_de_acidentes_nao_fatais += nao_fatal[i]
    totalsem_vitimas += sem_vitimas[i]
    i += 1


print(f'4.a) A quantidade de ve�culos no pa�s: {totalveiculos}')
print(f'4.b) A quantidade de acidentes no pa�s: {total_de_acidentes}')
print(
    f'4.c) A quantidade de acidentes com v�timas fatais no pa�s: {totalfatal}')
print(
    f'4.d) O munic�pio com maior n�mero de acidentes: {nome[MAIS]} ({mais_acidentes})')
print(
    f'4.d) O munic�pio com menor n�mero de acidentes: {nome[MENOS]} ({menos_acidentes})')
print(f'\n5.a) A m�dia de ve�culos por munic�pios: {totalveiculos/i}')
print(
    f'5.b) A m�dia de acidentes com v�timas fatais por munic�pios: {totalfatal/i}')
print(
    f'5.b) A m�dia de acidentes com v�timas n�o-fatais por munic�pios: {total_de_acidentes_nao_fatais/i}')
print(
    f'5.b) A m�dia de acidentes sem v�timas por munic�pios: {totalsem_vitimas/i}')
print(f'\n5.c) O maior IVT � de {IVTH} e pertence ao munic�pio {nome[H]}')
print(f'5.d) Nome do munic�pio: {nome[H]}')
print(f'5.d) Quantidade de ve�culos de {nome[H]}: {veiculos[H]}')
print(f'5.d) Total de acidentes com v�timas fatais em {nome[H]}: {fatal[H]}')
print(
    f'5.d) Total de acidentes com v�timas n�o-fatais em {nome[H]}: {nao_fatal[H]}')
print(f'5.d) Total de acidentes sem v�timas em {nome[H]}: {sem_vitimas[H]}')
print(f'\n5.c) O menor IVT � de {IVTL} e pertence ao munic�pio {nome[L]}')
print(f'5.d) Nome do munic�pio: {nome[L]}')
print(f'5.d) Quantidade de ve�culos de {nome[L]}: {veiculos[L]}')
print(f'5.d) Total de acidentes com v�timas fatais em {nome[L]}: {fatal[L]}')
print(
    f'5.d) Total de acidentes com v�timas n�o-fatais em {nome[L]}: {nao_fatal[L]}')
print(f'5.d) Total de acidentes sem v�timas em {nome[L]}: {sem_vitimas[L]}')
