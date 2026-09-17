#stack - pilha
#queue - fila
#priority queue - fila de prioridade
#impossible - impossível
#not sure - não tenho certeza
#heapq() - 
from collections import deque
#deque - fila de duas pontas
import heapq

while True:
    try: 
        N = int(input())
    except EOFError:
        break

    pilha = []
    fila = deque()
    prioridade = []

    epilha = True
    #Pilha primeiro Fila depois
    efila = True
    eprioridade = True

    for _ in range(N):
        operacao, valor = map(int, input().split())

        if operacao == 1:
            pilha.append(valor)
        #pilha.append() adiciona um elemento no final da pilha
            fila.append(valor)
        #fila.append() adiciona um elemento no final da fila
            heapq.heappush(prioridade, -valor)
        #heapq.heappush() adiciona um elemento na fila de prioridade
        else:
            if not pilha:
                epilha = False
            else:
                removido = pilha.pop()
            #pop() remove o último elemento da pilha
                if removido != valor:
                    epilha = False

            if not fila:
                efila = False
            else:
                removido = fila.popleft()
            #popleft() remove o primeiro elemento da fila
                if removido != valor:
                    efila = False

            if not prioridade:
                eprioridade = False
            else:
                removido = -heapq.heappop(prioridade)
            #heapq.heappop() remove o elemento de maior prioridade da fila
            #de prioridade
                if removido != valor:
                    eprioridade = False

    possibilidades = sum([epilha, efila, eprioridade]) 

    if possibilidades == 0:
        print("impossible")

    elif possibilidades > 1:
        print("not sure")

    elif epilha:
        print("stack")

    elif efila:
        print("queue")

    elif eprioridade:
        print("priority queue")

    else:
        print("priority queue")
    

