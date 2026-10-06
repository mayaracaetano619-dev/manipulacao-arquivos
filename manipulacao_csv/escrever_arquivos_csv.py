import csv

def criar_csv():
    with open("alunos.csv", "w", newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Curso"])

        escritor.writerow(["Mayara", 16, "DEV"])
        escritor.writerow(["Julia", 17, "HTML"])
        escritor.writerow(["Sophia", 16, "Python"])

#criar_csv()

def salvar_alunos():
    alunos = [
        ["Mayara", 16, "DEV"],
        ["Julia", 17, "HTML"],
        ["Sophia", 16, "Python"],
        ["Maria", 15, "IoT"]
    ]

    with open("novos_alunos.csv", "w", newline="", encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Curso"])

        escritor.writerows(alunos)

#salvar_alunos()

def ler_csv():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor)
        for linha in leitor:
            print(linha[0])

ler_csv()
