def contar_caracteres():
    with open("nomes.txt", "r", encoding='utf-8') as arquivo:
        texto = arquivo.read()
    quantidade = len(texto)
    print("Quantidade de caracteres:", quantidade)

contar_caracteres()