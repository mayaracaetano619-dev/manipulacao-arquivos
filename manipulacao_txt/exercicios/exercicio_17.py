def calcular_estoque():
    produtos = []
    with open('produtos.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(';')
            produto = {
                'nome': nome,
                'preco': float(preco),
                'quantidade': int(quantidade)
            }
            produtos.append(produto)

    valor_total = 0
    for produto in produtos:
        valor = produto['preco'] * produto['quantidade']
        valor_total = valor_total + valor
    print(f'Valor total do estoque: R$ {valor_total}')

calcular_estoque()