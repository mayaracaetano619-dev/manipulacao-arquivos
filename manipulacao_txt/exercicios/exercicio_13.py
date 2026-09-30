def criar_aquivo():
    with open('notas.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('10\n'
                      '9.5\n'
                      '8.5\n'
                      '7.5\n'
                      '6.5\n'
                      '9.0\n')
criar_aquivo()

def menu_arquivo():
    while True:
        print('=======Menu de Operações=======')
        print('1 - Ler arquivo')
        print('2 - Adicionar texto')
        print('3 - Sobrescrever arquivo')
        print('0 - Sair')

        opcao = input('Escolha: ')

        if opcao == '1':
            with open('notas.txt', 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()

            print(conteudo)

        elif opcao == '2':
            texto = input('Digite o texto: ')

            with open('notas.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(texto + '\n')

        elif opcao == '3':
            texto = input('Digite o novo texto: ')

            with open('notas.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.write(texto)

        elif opcao == '0':
            print('Programa encerrado.')
            break

        else:
            print('Opção inválida!')


menu_arquivo()