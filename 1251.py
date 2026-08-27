# Lê a quantidade de casos de teste
n = int(input())
# int() transforma o que foi digitado em número inteiro
# input() lê uma informação digitada pelo usuário


# Repetirá o código n vezes
for caso in range(n):
    # caso vai assumir os valores 0, 1, 2, ..., n-1

    # Lê o texto que será analisado
    texto = input()

    # Cria um dicionário vazio
    # Ele vai guardar:
    # código ASCII/Unicode do caractere -> quantidade de vezes que apareceu
    frequencia = {}


    # Percorre cada caractere do texto
    for caractere in texto:

        # ord() transforma o caractere em seu código Unicode
        # Exemplo:
        # ord('a') = 97
        # ord('b') = 98
        # ord('A') = 65
        codigo = ord(caractere)


        # Verifica se esse código ainda NÃO existe no dicionário
        if codigo not in frequencia:

            # Se não existe, cria a chave e começa com quantidade 0
            frequencia[codigo] = 0


        # Aumenta em 1 a quantidade de vezes que o caractere apareceu
        frequencia[codigo] += 1


    # Pega todas as chaves do dicionário
    # As chaves são os códigos dos caracteres
    caracteres = list(frequencia.keys())


    # Organiza os códigos de acordo com a regra abaixo
    caracteres.sort(
        key=lambda codigo: (frequencia[codigo], -codigo)
    )


    # Percorre os códigos já ordenados
    for codigo in caracteres:

        # Mostra:
        # código do caractere + quantidade de vezes que apareceu
        print(codigo, frequencia[codigo])


    # Verifica se este NÃO é o último caso de teste
    if caso < n - 1:

        # Se ainda existem outros casos, imprime uma linha vazia
        print()