m = input()
qtd_senhas = int(input())
dict_senhas = {}

m = m.title()
m = m.replace(' ', '')
m = m.replace('a', '@')
m = m.replace('E', '%')
m = m.replace('e', '!')
m = m.replace('i', '@')
m = m.replace('o', '#')
m = m.replace('u', '$')

lista = []

for itens_trocados in m:
    lista.append(itens_trocados)

senha_inicial = ''.join(lista)

numero = 0
while qtd_senhas > len(dict_senhas):
    menor_q6 = int(input())

    while menor_q6 < 6:
        menor_q6 = int(input())

    comeco_da_senha = senha_inicial[numero:numero+5]
    meio_da_senha = senha_inicial[-5:]
    final_da_senha = senha_inicial[menor_q6:menor_q6+5]
    senha = comeco_da_senha + meio_da_senha + final_da_senha
    senha = senha[::-1]
    print(senha)

    usuario = input()
    if usuario.lower() == 's':
        proximo_usuario = input()
        dict_senhas[proximo_usuario] = senha
        numero += 1
print(dict_senhas)
