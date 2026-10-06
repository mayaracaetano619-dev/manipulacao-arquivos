import csv


def ler_treinadores():
    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        treinadores = list(leitor)

    return treinadores


def menu():
    treinadores = ler_treinadores()

    while True:
        print(f"===== TREINADORES POKÉMON =====")
        print(f"1 - Listar todos os treinadores")
        print(f"2 - Buscar treinador pelo nome")
        print(f"3 - Listar treinadores de uma região")
        print(f"4 - Mostrar treinador com maior nível")
        print(f"5 - Mostrar treinador com menor nível")
        print(f"0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            for treinador in treinadores:
                print(f"{treinador['nome']} - {treinador['regiao']} - Nível: {treinador['nivel']}")

        elif opcao == "2":
            nome = input("Digite o nome do treinador: ")

            encontrado = False

            for treinador in treinadores:
                if treinador["nome"].lower() == nome.lower():
                    print(f"Nome: {treinador['nome']}")
                    print(f"Região: {treinador['regiao']}")
                    print(f"Nível: {treinador['nivel']}")
                    encontrado = True

            if encontrado == False:
                print(f"Treinador não encontrado.")

        elif opcao == "3":
            regiao = input("Digite a região: ")

            encontrado = False

            for treinador in treinadores:
                if treinador["regiao"].lower() == regiao.lower():
                    print(f"{treinador['nome']} - Nível: {treinador['nivel']}")
                    encontrado = True

            if encontrado == False:
                print(f"Nenhum treinador encontrado nessa região.")

        elif opcao == "4":
            maior = treinadores[0]

            for treinador in treinadores:
                if int(treinador["nivel"]) > int(maior["nivel"]):
                    maior = treinador

            print(f"\nTreinador com maior nível:")
            print(f"Nome: {maior['nome']}")
            print(f"Região: {maior['regiao']}")
            print(f"Nível: {maior['nivel']}")

        elif opcao == "5":
            menor = treinadores[0]

            for treinador in treinadores:
                if int(treinador["nivel"]) < int(menor["nivel"]):
                    menor = treinador

            print(f"\nTreinador com menor nível:")
            print(f"Nome: {menor['nome']}")
            print(f"Região: {menor['regiao']}")
            print(f"Nível: {menor['nivel']}")

        elif opcao == "0":
            print(f"Programa encerrado.")
            break

        else:
            print(f"Opção inválida.")


menu()