import csv

def ler_treinadores():
    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        leitores = csv.DictReader(arquivo)
        treinadores = list(leitores)

    return treinadores


def menu():
    treinadores = ler_treinadores()

    while True:
        print(f"==== CONSULTA DE TREINADORES ====")
        print(f"1 - Listar todos os treinadores")
        print(f"2 - Buscar treinador por nome")
        print(f"3 - Listar treinadores por região")
        print(f"4 - Treinador com maior nível")
        print(f"5 - Treinador com menor nível")
        print(f"0 - Sair")

        opcao = input(f"Digite uma opção: ")

        if opcao == "1":
            for treinador in treinadores:
                print(f"Nome: {treinador['nome']} - Região: {treinador['regiao']} - Nível: {treinador['nivel']}")

        elif opcao == "2":
            nome = input(f"Digite o nome do treinador: ")
            encontrado = False

            for treinador in treinadores:
                if treinador["nome"] == nome:
                    print(f"Nome: {treinador['nome']}")
                    print(f"Região: {treinador['regiao']}")
                    print(f"Nível: {treinador['nivel']}")
                    encontrado = True

            if encontrado == False:
                print(f"Treinador não encontrado.")

        elif opcao == "3":
            regiao = input(f"Digite a região: ")
            encontrado = False

            for treinador in treinadores:
                if treinador["regiao"] == regiao:
                    print(f"Nome: {treinador['nome']} - Região: {treinador['regiao']} - Nível: {treinador['nivel']}")
                    encontrado = True

            if encontrado == False:
                print(f"Nenhum treinador encontrado nessa região.")

        elif opcao == "4":
            maior = treinadores[0]

            for treinador in treinadores:
                if int(treinador["nivel"]) > int(maior["nivel"]):
                    maior = treinador

            print(f"Treinador com maior nível: {maior['nome']} - Nível: {maior['nivel']}")

        elif opcao == "5":
            menor = treinadores[0]

            for treinador in treinadores:
                if int(treinador["nivel"]) < int(menor["nivel"]):
                    menor = treinador

            print(f"Treinador com menor nível: {menor['nome']} - Nível: {menor['nivel']}")

        elif opcao == "0":
            print(f"Programa encerrado.")
            break

        else:
            print(f"Opção inválida.")


menu()
