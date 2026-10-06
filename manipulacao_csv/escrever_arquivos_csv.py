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

#ler_csv()

def exibir_alunos():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        alunos = csv.DictReader(arquivo)

        for aluno in alunos:
            print(aluno)

exibir_alunos()

def cadastrar_alunos():
    with open("novos_alunos.csv", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.seek(0,2)
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        curso = input("Digite o curso do aluno: ")

        escritor = csv.writer(arquivo)
        escritor.writerow([nome, idade, curso])

        arquivo.seek(0)
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            print(linha)

#cadastrar_alunos()

def deletar_alunos():
    with open("novos_alunos.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        alunos = list(leitor)

    with open("novos_alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
        cabecalho = ["Nome", "Idade", "Curso"]
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)

        escritor.writeheader()

        aluno_apagar = input("Digite o nome do aluno que deseja apagar:")

        for aluno in alunos:
            if aluno["Nome"] == aluno_apagar:
                escritor.writerow(aluno)

deletar_alunos()














