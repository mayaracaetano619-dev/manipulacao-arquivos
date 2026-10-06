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
        print(f"==== CONSULTA DE POKÉMON ====")
        print(f"1 - Listar Pokémon de um treinador")
        print(f"2 - Contar Pokémon de um treinador")
        print(f"3 - Pokémon de maior nível")
        print(f"4 - Pokémon de menor nível")
        print(f"5 - Listar Pokémon por tipo")
        print(f"0 - Voltar ao menu")

        opcao = input(f"Digite uma opção: ")

        if opcao == "1":
            nome = input(f"Digite o nome do treinador: ")
            lista = []

            for treinador in treinadores:
                if treinador["nome"] == nome:
                    for pokemon in pokemons:
                        if pokemon["treinador"] == nome:
                            lista.append(pokemon)

            if len(lista) == 0:
                print(f"Nenhum Pokémon encontrado.")
            else:
                for pokemon in lista:
                    print(f"{pokemon['nome']} - Tipo: {pokemon['tipo']} - Nível: {pokemon['nivel']}")

        elif opcao == "2":
            nome = input(f"Digite o nome do treinador: ")
            quantidade = 0

            for pokemon in pokemons:
                if pokemon["treinador"] == nome:
                    quantidade = quantidade + 1

            print(f"O treinador {nome} possui {quantidade} Pokémon.")

        elif opcao == "3":
            nome = input(f"Digite o nome do treinador: ")
            maior = None

            for pokemon in pokemons:
                if pokemon["treinador"] == nome:
                    if maior is None or int(pokemon["nivel"]) > int(maior["nivel"]):
                        maior = pokemon

            if maior is None:
                print(f"Nenhum Pokémon encontrado.")
            else:
                print(f"Pokémon de maior nível: {maior['nome']} - Nível: {maior['nivel']}")

        elif opcao == "4":
            nome = input(f"Digite o nome do treinador: ")
            menor = None

            for pokemon in pokemons:
                if pokemon["treinador"] == nome:
                    if menor is None or int(pokemon["nivel"]) < int(menor["nivel"]):
                        menor = pokemon

            if menor is None:
                print(f"Nenhum Pokémon encontrado.")
            else:
                print(f"Pokémon de menor nível: {menor['nome']} - Nível: {menor['nivel']}")

        elif opcao == "5":
            tipo = input(f"Digite o tipo do Pokémon: ")
            encontrado = False

            for pokemon in pokemons:
                if pokemon["tipo"] == tipo:
                    print(f"{pokemon['nome']} - Tipo: {pokemon['tipo']} - Nível: {pokemon['nivel']}")
                    encontrado = True

            if encontrado == False:
                print(f"Nenhum Pokémon desse tipo foi encontrado.")

        elif opcao == "0":
            print(f"Voltando...")
            break

        else:
            print(f"Opção inválida.")


menu()
