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

def menu():
    treinadores = ler_treinadores()
    pokemons = ler_pokemons()

    while True:
        print(f"==== RELATÓRIO ====")
        print(f"1 - Relatório de treinador")
        print(f"2 - Média dos níveis dos Pokémon de um treinador")
        print(f"3 - Média dos níveis por tipo")
        print(f"4 - Quantidade de Pokémon por treinador")
        print(f"5 - Quantidade de Pokémon por tipo")
        print(f"6 - Treinadores acima de um nível")
        print(f"0 - Sair")

        opcao = input(f"Digite uma opção: ")

        if opcao == "1":
            nome = input(f"Digite o nome do treinador: ")

            for treinador in treinadores:
                if treinador["nome"] == nome:
                    print(f"Nome: {treinador['nome']}")
                    print(f"Região: {treinador['regiao']}")
                    print(f"Nível: {treinador['nivel']}")

                    quantidade = 0

                    for pokemon in pokemons:
                        if pokemon["treinador"] == nome:
                            quantidade = quantidade + 1

                    print(f"Quantidade de Pokémon: {quantidade}")

        elif opcao == "2":
            nome = input(f"Digite o nome do treinador: ")
            soma = 0
            quantidade = 0

            for pokemon in pokemons:
                if pokemon["treinador"] == nome:
                    soma = soma + int(pokemon["nivel"])
                    quantidade = quantidade + 1

            if quantidade > 0:
                media = soma / quantidade
                print(f"Média dos níveis: {media:.2f}")
            else:
                print(f"Nenhum Pokémon encontrado.")

        elif opcao == "3":
            tipo = input(f"Digite o tipo: ")
            soma = 0
            quantidade = 0

            for pokemon in pokemons:
                if pokemon["tipo"] == tipo:
                    soma = soma + int(pokemon["nivel"])
                    quantidade = quantidade + 1

            if quantidade > 0:
                media = soma / quantidade
                print(f"Média dos níveis do tipo {tipo}: {media:.2f}")
            else:
                print(f"Nenhum Pokémon encontrado.")

        elif opcao == "4":
            quantidade = {}

            for pokemon in pokemons:
                treinador = pokemon["treinador"]

                if treinador not in quantidade:
                    quantidade[treinador] = 1
                else:
                    quantidade[treinador] = quantidade[treinador] + 1

            for treinador in quantidade:
                print(f"{treinador}: {quantidade[treinador]} Pokémon")

        elif opcao == "5":
            quantidade = {}

            for pokemon in pokemons:
                tipo = pokemon["tipo"]

                if tipo not in quantidade:
                    quantidade[tipo] = 1
                else:
                    quantidade[tipo] = quantidade[tipo] + 1

            for tipo in quantidade:
                print(f"{tipo}: {quantidade[tipo]} Pokémon")

        elif opcao == "6":
            nivel = int(input(f"Digite o nível: "))

            for treinador in treinadores:
                if int(treinador["nivel"]) > nivel:
                    print(f"{treinador['nome']} - Nível: {treinador['nivel']}")

        elif opcao == "0":
            print(f"Programa encerrado.")
            break

        else:
            print(f"Opção inválida.")


menu()
