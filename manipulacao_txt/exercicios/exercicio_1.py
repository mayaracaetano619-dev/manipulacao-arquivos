def criar_arquivo():
    with open('mensagem.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Olá mundo!\n'
                      'Estou aprendendo Python.\n'
                      'Estou estudando manipulação de arquivos.\n')
criar_arquivo()
def ler_arquivo():
    with open('mensagem.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(f'O conteúdo do arquivo mensagem é: {conteudo}')

ler_arquivo()
