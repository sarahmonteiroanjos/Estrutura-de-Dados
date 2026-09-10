while True:
    #repetição
    n = int(input())
    #input lê o que o usuário digitou

    if n == 0:
    #0 feicha a repetição
        break

    entrada = input().split()
    saida = input().split()
    #split separa pelos espaços

    pilha = []
    operacoes = []

    i = 0

    for vagao in entrada:
        pilha.append(vagao)
        operacoes.append("I")

        while pilha and i < n and pilha[-1] == saida[i]:
            pilha.pop()
            operacoes.append("R")
            i += 1
            #pop remove pilha
            #append inclui

    if i == n:
        print("".join(operacoes))
    else:
        print("".join(operacoes), "Impossivel")