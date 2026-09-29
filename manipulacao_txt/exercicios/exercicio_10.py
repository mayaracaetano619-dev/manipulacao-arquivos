def separar_numeros():
    pares = []
    impares = []
    with open("numeros.txt", "r", encoding='utf-8') as arquivo:
        for linha in arquivo:
            numero = int(linha.strip())
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

separar_numeros()