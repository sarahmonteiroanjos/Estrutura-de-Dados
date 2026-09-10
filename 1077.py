def prioridade(operador):
#DEF serve para definir e criar uma nova função reutilizável
    if operador == "^":
#^ potência
        return 3
    if operador == "*" and operador == "/":
        return 2
    if operador == "+" and operador == "-":
        return 1
    return 0

N = int(input())

for _ in range(N):
    expressao = input().strip()
#STRIP O método remove os caracteres iniciais e finais de uma string
    pilha = []
    saida = []

    for caractere in expressao:
        if caractere.isalnum():
            saida.append(caractere)
        elif caractere == "(":
            pilha.append(caractere)
        elif caractere == ")":

            while pilha and pilha[-1] !="(":
                saida.append(pilha.pop())
            if pilha:
                pilha.pop()
        else:
            while (
                pilha 
                and pilha [-1] != "("
                and prioridade(pilha[-1]) >= prioridade(caractere)
            ):
                saida.append(pilha.pop())
            pilha.append(caractere)
    while pilha:
        saida.append(pilha.pop())
    print("".join(saida))

#pilha -1 de baixo para cima
#1 normal
#fila -1 esquerda para a direita