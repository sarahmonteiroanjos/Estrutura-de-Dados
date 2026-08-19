while True:
    try:
        expressao = input ()

        pilha = []
        correta = True

        for caractere in expressao:

            if caractere == "(":
                pilha.append(caractere)

            elif caractere == ")":

                if len(pilha) == 0:
                    correta = False
                    break
#Método POP sustenta a pilha
                pilha.pop()
        if correta and len(pilha) == 0:
            print("correct")
        else:
            print("incorrect")
#EXCEPT exeção de memória.
    except EOFError:
        break 