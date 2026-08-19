from collections import deque
#DEQUE estrutura das filas
while True:
    N = int (input())

    if N == 0:
        break

    fila = deque(range(1, N + 1))
#RANGE (inicio(contador), Condição, inerente(decremento))
    descartadas = []

    while len(fila) > 1:
        descartadas.append(str(fila.popleft()))

        fila.append(fila.popleft())
#Len armazena a fila
#STR = string
#POPLeft descarta o número para a direita
    print("Discarded cards", ", ".join(descartadas))
    print("Remaining card:" , fila[0])
#Discarded descarte de cartas
#Join juntar
#Remaining = Cartas remanecentes