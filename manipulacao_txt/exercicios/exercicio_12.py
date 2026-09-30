def classificar_alunos():
    alunos = []
    with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(';')
            aluno = {
                'nome': nome,
                'nota': nota
            }
            alunos.append(aluno)

    for aluno in alunos:
        if aluno['nota'] >= 6:
            situacao = 'Aprovado'
        elif aluno['nota'] >= 4:
            situacao = 'Recuperação'
        else:
            situacao = 'Reprovado'
        print(f"{aluno['nome']} - {aluno['nota']} - {situacao}")


classificar_alunos()