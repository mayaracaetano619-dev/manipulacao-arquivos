def criar_arquivo():
    with open('nomes.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Ana\n')
        arquivo.write('Bruno\n')
        arquivo.write('Carlos\n')
        arquivo.write('Daniela\n')
        arquivo.write('Eduardo\n')
        arquivo.write('Fernando\n')
        arquivo.write('Gabriel\n')
criar_arquivo()

def contar_linhas():
    quantidade = 0
    with open("nomes.txt", "r", encoding='utf-8') as arquivo:
        for linha in arquivo:
            quantidade += 1
    print(f"O arquivo possui {quantidade} linhas.")


contar_linhas()