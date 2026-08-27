# N = quantidade de casos/linhas que serão lidos
n = int(input())

# Repete o código n vezes
# O "_" significa que não precisamos usar o número da repetição
for _ in range(n):

    # Lê uma linha e separa as palavras pelo espaço
    palavras = input().split()

    # Organiza as palavras pelo tamanho
    # key=len → usa o tamanho da palavra como critério
    # reverse=True → coloca da maior para a menor
    palavras.sort(key=len, reverse=True)

    # Junta todas as palavras novamente em uma única frase
    # " ".join() coloca um espaço entre cada palavra
    print(" ".join(palavras))
