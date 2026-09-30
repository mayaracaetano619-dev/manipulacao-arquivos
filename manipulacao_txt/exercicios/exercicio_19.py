def criar_arquivo():
        with open('vendas.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write('Ana;Notebook;3500\n')
            arquivo.write('Bruno;Mouse;100\n')
            arquivo.write('Ana;Teclado;200\n')
            arquivo.write('Carlos;Monitor;1200\n')
            arquivo.write('Bruno;Notebook;3500\n')

criar_arquivo()

def gerar_relatorio():
    vendas = []
    with open('vendas.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            vendedor, produto, valor = linha.strip().split(';')
            venda = {
                'vendedor': vendedor,
                'produto': produto,
                'valor': float(valor)
            }
            vendas.append(venda)

    total = 0
    quantidade_vendas = {}

    for venda in vendas:
        print(venda)

        total = total + venda['valor']
        vendedor = venda['vendedor']

        if vendedor in quantidade_vendas:
            quantidade_vendas[vendedor] += 1
        else:
            quantidade_vendas[vendedor] = 1

    print(f'TOTAL DE VENDAS: R$ {total}')

    print('Quantidade de vendas:')

    for vendedor in quantidade_vendas:
        print(f'{vendedor}: {quantidade_vendas[vendedor]}')


gerar_relatorio()