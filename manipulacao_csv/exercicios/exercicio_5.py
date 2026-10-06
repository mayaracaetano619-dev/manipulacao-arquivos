import csv

def ler_pokemons():
    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        leitores = csv.DictReader(arquivo)
        pokemons = list(leitores)
    return pokemons

def ler_treinadores():
    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        leitores = csv.DictReader(arquivo)
        treinadores = list(leitores)
    return treinadores

def menu():
    pokemons = ler_pokemons()
    treinadores = ler_treinadores()

    while True:
        print(f"==== GERENCIAMENTO DE POKÉMON ====")
        print(f"1 - Listar Pokémon")
        print(f"2 - Buscar Pokémon")
        print(f"3 - Adicionar Pokémon")
        print(f"4 - Alterar nível")
        print(f"5 - Remover Pokémon")
        print(f"6 - Salvar alterações")
        print(f"0 - Sair")

        opcao = input(f"Digite uma opção: ")

        if opcao == "1":
            for pokemon in pokemons:
                print(f"{pokemon['nome']} - {pokemon['tipo']} - Nível: {pokemon['nivel']} - Treinador: {pokemon['treinador']}")

        elif opcao == "2":
            nome = input(f"Digite o nome do Pokémon: ")
            encontrado = False

            for pokemon in pokemons:
                if pokemon["nome"] == nome:
                    print(f"Nome: {pokemon['nome']}")
                    print(f"Tipo: {pokemon['tipo']}")
                    print(f"Nível: {pokemon['nivel']}")
                    print(f"Treinador: {pokemon['treinador']}")
                    encontrado = True

            if encontrado == False:
                print(f"Pokémon não encontrado.")

        elif opcao == "3":
            nome = input(f"Digite o nome do Pokémon: ")
            tipo = input(f"Digite o tipo do Pokémon: ")
            nivel = input(f"Digite o nível do Pokémon: ")
            treinador = input(f"Digite o nome do treinador: ")

            existe = False

            for pokemon in pokemons:
                if pokemon["nome"] == nome:
                    existe = True

            treinador_existe = False

            for item in treinadores:
                if item["nome"] == treinador:
                    treinador_existe = True

            if nome == "":
                print(f"O nome não pode ficar vazio.")

            elif tipo == "":
                print(f"O tipo não pode ficar vazio.")

            elif nivel == "":
                print(f"O nível não pode ficar vazio.")

            elif int(nivel) < 1 or int(nivel) > 100:
                print(f"O nível deve estar entre 1 e 100.")

            elif existe == True:
                print(f"Esse Pokémon já existe.")

            elif treinador_existe == False:
                print(f"Treinador não encontrado.")

            else:
                novo_pokemon = {
                    "nome": nome,
                    "tipo": tipo,
                    "nivel": nivel,
                    "treinador": treinador
                }

                pokemons.append(novo_pokemon)

                print(f"Pokémon adicionado com sucesso.")

        elif opcao == "4":
            nome = input(f"Digite o nome do Pokémon: ")
            encontrado = False

            for pokemon in pokemons:
                if pokemon["nome"] == nome:
                    novo_nivel = input(f"Digite o novo nível: ")

                    if int(novo_nivel) >= 1 and int(novo_nivel) <= 100:
                        pokemon["nivel"] = novo_nivel
                        print(f"Nível alterado com sucesso.")
                    else:
                        print(f"O nível deve estar entre 1 e 100.")

                    encontrado = True

            if encontrado == False:
                print(f"Pokémon não encontrado.")

        elif opcao == "5":
            nome = input(f"Digite o nome do Pokémon: ")
            encontrado = False

            for pokemon in pokemons:
                if pokemon["nome"] == nome:
                    pokemons.remove(pokemon)
                    encontrado = True
                    print(f"Pokémon removido com sucesso.")
                    break

            if encontrado == False:
                print(f"Pokémon não encontrado.")

        elif opcao == "6":
            with open("pokemons_atualizados.csv", "w", newline="", encoding="utf-8") as arquivo:
                campos = ["nome", "tipo", "nivel", "treinador"]

                escritor = csv.DictWriter(arquivo, fieldnames=campos)

                escritor.writeheader()
                escritor.writerows(pokemons)

            print(f"Alterações salvas em pokemons_atualizados.csv.")

        elif opcao == "7":
            print(f"Programa encerrado.")
            break

        else:
            print(f"Opção inválida.")


menu()
