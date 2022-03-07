nacionalidade = input()
ocupacao = input()
qtd = int(input())
calibre = int(input())

if nacionalidade == "E":
    if qtd == 0:
        print("Liberado")
    else:
        print("Barrado")
else:
    if ocupacao == "M":
        print("Liberado")
    elif ocupacao == "T" or ocupacao == "O":
        if qtd <= 1:
            if calibre <= 22:
                print("Liberado")
            else:
                print("Barrado")
        else:
            print("Barrado")
    else:
        if qtd <= 2:
            if calibre <= 38:
                print("Liberado")
            else:
                print("Barrado")
        else:
            print("Barrado")
