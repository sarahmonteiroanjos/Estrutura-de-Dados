# Cria um loop que continuará até encontrarmos o fim da entrada
while True:

    try:
        # Tenta ler a quantidade de telefones
        n = int(input())

    # EOFError acontece quando não há mais dados para ler
    except EOFError:
        # Encerra o while
        break


    # Cria uma lista vazia para guardar os telefones
    telefones = []


    # Repete n vezes
    for _ in range(n):

        # Lê um telefone, remove espaços extras
        # e adiciona o telefone na lista
        telefones.append(input().strip())


    # Ordena os telefones em ordem crescente
    telefones.sort()


    # Variável que vai guardar a economia total
    economia = 0


    # Começa no índice 1 porque vamos comparar
    # cada telefone com o telefone anterior
    for i in range(1, n):

        # Pega o telefone que está antes do atual
        anterior = telefones[i - 1]

        # Pega o telefone atual
        atual = telefones[i]


        # Começamos a comparar os caracteres
        # a partir da posição 0
        J = 0


        # Continua enquanto:
        # 1. ainda houver caracteres no telefone atual
        # 2. os caracteres das duas strings forem iguais
        while J < len(atual) and atual[J] == anterior[J]:

            # Avança para o próximo caractere
            J += 1


        # Adiciona à economia a quantidade de caracteres
        # iguais no começo dos dois telefones
        economia += J


    # Mostra a economia total
    print(economia)