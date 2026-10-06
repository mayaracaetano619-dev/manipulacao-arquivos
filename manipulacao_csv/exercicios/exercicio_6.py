import csv

def ler_treinadores():
    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        leitores = csv.DictReader(arquivo)
        treinadores = list(leitores)
    return treinadores

def ler_pokemons():
    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        leitores = csv.DictReader(arquivo)
        pokemons = list(leitores)
    return pokemons

def calcular_resultados(treinadores, pokemons):
    resultados = []

    for treinador in treinadores:
        nome = treinador["nome"]
        soma_niveis = 0
        quantidade = 0

        for pokemon in pokemons:
            if pokemon["treinador"] == nome:
                soma_niveis = soma_niveis + int(pokemon["nivel"])
                quantidade = quantidade + 1

        pontuacao = int(treinador["nivel"]) + soma_niveis

        resultado = {
            "treinador": nome,
            "regiao": treinador["regiao"],
            "nivel_treinador": treinador["nivel"],
            "quantidade_pokemons": quantidade,
            "soma_niveis": soma_niveis,
            "pontuacao": pontuacao
        }

        resultados.append(resultado)
    return resultados

def ordenar_resultados(resultados):
    lista = []

    maior_pontuacao = 0

    for resultado in resultados:
        if resultado["pontuacao"] > maior_pontuacao:
            maior_pontuacao = resultado["pontuacao"]

    while len(lista) < len(resultados):
        maior = None

        for resultado in resultados:
            if resultado not in lista:
                if resultado["pontuacao"] == maior_pontuacao:
                    maior = resultado

        if maior is not None:
            lista.append(maior)

        maior_pontuacao = maior_pontuacao - 1
    return lista

def menu():
    treinadores = ler_treinadores()
    pokemons = ler_pokemons()

    while True:
        print(f"==== CAMPEONATO POKÉMON ====")
        print(f"1 - Listar treinadores")
        print(f"2 - Consultar equipe")
        print(f"3 - Calcular pontuação")
        print(f"4 - Classificação")
        print(f"5 - Gerar CSV do campeonato")
        print(f"0 - Sair")

        opcao = input(f"Digite uma opção: ")

        if opcao == "1":
            for treinador in treinadores:
                print(f"{treinador['nome']} - Região: {treinador['regiao']} - Nível: {treinador['nivel']}")

        elif opcao == "2":
            nome = input(f"Digite o nome do treinador: ")
            encontrado = False

            for pokemon in pokemons:
                if pokemon["treinador"] == nome:
                    print(f"{pokemon['nome']} - Tipo: {pokemon['tipo']} - Nível: {pokemon['nivel']}")
                    encontrado = True

            if encontrado == False:
                print(f"Nenhum Pokémon encontrado.")

        elif opcao == "3":
            resultados = calcular_resultados(treinadores, pokemons)

            for resultado in resultados:
                print(f"{resultado['treinador']} - Pontuação: {resultado['pontuacao']}")

        elif opcao == "4":
            resultados = calcular_resultados(treinadores, pokemons)
            resultados = ordenar_resultados(resultados)

            posicao = 1

            for resultado in resultados:
                print(f"{posicao}º lugar - {resultado['treinador']} - Pontuação: {resultado['pontuacao']}")
                posicao = posicao + 1

        elif opcao == "5":
            resultados = calcular_resultados(treinadores, pokemons)

            with open("resultado_campeonato.csv", "w", newline="", encoding="utf-8") as arquivo:
                campos = [
                    "treinador",
                    "regiao",
                    "nivel_treinador",
                    "quantidade_pokemons",
                    "soma_niveis",
                    "pontuacao"
                ]

                escritor = csv.DictWriter(arquivo, fieldnames=campos)

                escritor.writeheader()
                escritor.writerows(resultados)

            print(f"Arquivo resultado_campeonato.csv criado.")
            print(f"Quantidade de registros: {len(resultados)}")

        elif opcao == "0":
            print(f"Programa encerrado.")
            break

        else:
            print(f"Opção inválida.")


menu()
