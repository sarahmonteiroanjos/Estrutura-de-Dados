caso_de_teste = int(input())

for _ in range(caso_de_teste):
   caso_de_teste = input()
   
   pilha = []
   diamantes = 0
        
for caractere in caso_de_teste:

        if caractere == "<":
             pilha.append(caractere)
        elif caractere == ".":
             pass

        elif caractere == ">":

         if len(pilha) > 0:
            pilha.pop()
            diamantes += 1
                    
#Método POP sustenta a pilha
        print(diamantes)
#EXCEPT exeção de memória.
    