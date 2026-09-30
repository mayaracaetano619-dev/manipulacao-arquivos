def sistema_alunos():
    alunos = []

    with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            id, nome, idade, curso = linha.strip().split(';')

            aluno = {
                'id': int(id),
                'nome': nome,
                'idade': int(idade),
                'curso': curso
            }

            alunos.append(aluno)

    while True:
        print('\n===== SISTEMA DE ALUNOS =====')
        print('1 - Listar alunos')
        print('2 - Buscar aluno')
        print('3 - Cadastrar aluno')
        print('4 - Remover aluno')
        print('5 - Alterar aluno')
        print('6 - Sair')

        opcao = input('Escolha: ')

        if opcao == '1':
            for aluno in alunos:
                print(
                    f"{aluno['id']} - "
                    f"{aluno['nome']} - "
                    f"{aluno['idade']} anos"
                )

        elif opcao == '2':
            id_buscar = int(input('Digite o ID: '))

            encontrado = False

            for aluno in alunos:
                if aluno['id'] == id_buscar:
                    print('Aluno encontrado:')
                    print(aluno['nome'])
                    print(f"{aluno['idade']} anos")
                    print(aluno['curso'])

                    encontrado = True

            if encontrado == False:
                print('Aluno não encontrado!')

        elif opcao == '3':
            id = int(input('ID: '))
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            curso = input('Curso: ')

            aluno = {
                'id': id,
                'nome': nome,
                'idade': idade,
                'curso': curso
            }

            alunos.append(aluno)

            with open('alunos.txt', 'w', encoding='utf-8') as arquivo:
                for aluno in alunos:
                    arquivo.write(
                        f"{aluno['id']};"
                        f"{aluno['nome']};"
                        f"{aluno['idade']};"
                        f"{aluno['curso']}\n"
                    )

            print('Aluno cadastrado com sucesso!')

        elif opcao == '4':
            id_remover = int(input('Digite o ID: '))

            encontrado = False

            for aluno in alunos:
                if aluno['id'] == id_remover:
                    alunos.remove(aluno)
                    encontrado = True

            if encontrado == True:
                with open('alunos.txt', 'w', encoding='utf-8') as arquivo:
                    for aluno in alunos:
                        arquivo.write(
                            f"{aluno['id']};"
                            f"{aluno['nome']};"
                            f"{aluno['idade']};"
                            f"{aluno['curso']}\n"
                        )

                print('Aluno removido com sucesso!')
            else:
                print('Aluno não encontrado!')

        elif opcao == '5':
            id_alterar = int(input('Digite o ID: '))

            encontrado = False

            for aluno in alunos:
                if aluno['id'] == id_alterar:
                    aluno['nome'] = input('Novo nome: ')
                    aluno['idade'] = int(input('Nova idade: '))
                    aluno['curso'] = input('Novo curso: ')

                    encontrado = True

            if encontrado == True:
                with open('alunos.txt', 'w', encoding='utf-8') as arquivo:
                    for aluno in alunos:
                        arquivo.write(
                            f"{aluno['id']};"
                            f"{aluno['nome']};"
                            f"{aluno['idade']};"
                            f"{aluno['curso']}\n"
                        )

                print('Aluno alterado com sucesso!')
            else:
                print('Aluno não encontrado!')

        elif opcao == '6':
            print('Programa encerrado.')
            break

        else:
            print('Opção inválida!')


sistema_alunos()