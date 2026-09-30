def criar_aquivo():
    with open('tarefas.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Estudar Python\n')
        arquivo.write('Fazer exercícios\n')
        arquivo.write('Estudar banco de dados\n')

criar_aquivo()

def gerenciar_tarefas():
    tarefas = []

    with open('tarefas.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            tarefas.append(linha.strip())

    while True:
        print('=======Lista de Tarefas=======')
        print('1 - Adicionar tarefa')
        print('2 - Listar tarefas')
        print('3 - Remover tarefa')
        print('0 - Sair')

        opcao = input('Escolha: ')

        if opcao == '1':
            tarefa = input('Digite a tarefa: ')
            tarefas.append(tarefa)

            with open('tarefas.txt', 'w', encoding='utf-8') as arquivo:
                for tarefa in tarefas:
                    arquivo.write(tarefa + '\n')
                print('Tarefa adicionada!')

        elif opcao == '2':
            for tarefa in tarefas:
                print(tarefa)

        elif opcao == '3':
            tarefa = input('Digite a tarefa que deseja remover: ')

            if tarefa in tarefas:
                tarefas.remove(tarefa)

                with open('tarefas.txt', 'w', encoding='utf-8') as arquivo:
                    for tarefa in tarefas:
                        arquivo.write(tarefa + '\n')

                print('Tarefa removida!')
            else:
                print('Tarefa não encontrada!')

        elif opcao == '0':
            print('Programa encerrado.')
            break

        else:
            print('Opção inválida!')


gerenciar_tarefas()