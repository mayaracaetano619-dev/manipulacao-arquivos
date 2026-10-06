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


def ordenar_pokemons(pokemons):
    lista = []

    for nivel in range(100, 0, -1):
        for pokemon in pokemons:
            if int(pokemon["nivel"]) == nivel:
                lista.append(pokemon)

    return lista


def menu():
    treinadores = ler_treinadores()
    pokemons = ler_pokemons()

    while True:
        print(f"==== GERADOR DE CSV ====")
        print(f"1 - Listar treinadores")
        print(f"2 - Gerar CSV de um treinador")
        print(f"3 - Gerar CSV de todos os treinadores")
        print(f"0 - Sair")

        opcao = input(f"Digite uma opção: ")

        if opcao == "1":
            for treinador in treinadores:
                print(f"{treinador['nome']} - {treinador['regiao']}")

        elif opcao == "2":
            nome = input(f"Digite o nome do treinador: ")
            lista = []

            for pokemon in pokemons:
                if pokemon["treinador"] == nome:
                    lista.append(pokemon)

            if len(lista) == 0:
                print(f"Nenhum Pokémon encontrado.")
            else:
                nome_arquivo = f"pokemons_{nome}.csv"

                with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
                    campos = ["nome", "tipo", "nivel", "treinador"]

                    escritor = csv.DictWriter(arquivo, fieldnames=campos)

                    escritor.writeheader()
                    escritor.writerows(lista)

                print(f"Arquivo {nome_arquivo} criado.")
                print(f"Quantidade de registros: {len(lista)}")

        elif opcao == "3":
            lista = ordenar_pokemons(pokemons)

            with open("todos_pokemons_ordenados.csv", "w", newline="", encoding="utf-8") as arquivo:
                campos = ["nome", "tipo", "nivel", "treinador"]

                escritor = csv.DictWriter(arquivo, fieldnames=campos)

                escritor.writeheader()
                escritor.writerows(lista)

            print(f"Arquivo todos_pokemons_ordenados.csv criado.")
            print(f"Quantidade de registros: {len(lista)}")

        elif opcao == "0":
            print(f"Programa encerrado.")
            break

        else:
            print(f"Opção inválida.")


menu()
