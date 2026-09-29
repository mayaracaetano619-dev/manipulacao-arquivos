def buscar_nome():
    nome = input("Digite o nome que deseja pesquisar: ")
    nomes = []
    with open("nomes.txt", "r", encoding='utf-8') as arquivo:
        for linha in arquivo:
            nomes.append(linha.strip())

    if nome in nomes:
        print("Nome encontrado!")
    else:
        print("Nome não encontrado!")


buscar_nome()