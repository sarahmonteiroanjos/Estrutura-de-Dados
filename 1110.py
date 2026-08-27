from collections import deque
# Importa o deque (double-ended queue)
# É uma estrutura parecida com uma fila.
# Ela permite retirar elementos do começo e adicionar no final



while True:
    # Cria um loop infinito.
    # Ele só vai parar quando encontrarmos N = 0.

    N = int(input())
    # input() → lê o valor digitado
    # int() → transforma o valor em número inteiro
    # N → quantidade de cartas


    if N == 0:
        # Verifica se N é igual a 0.

        break
        # break → interrompe o while True e encerra o programa.


    fila = deque(range(1, N + 1))
    # range(1, N + 1) cria os números das cartas.
    # Se N = 7:
    # range(1, 8) → 1, 2, 3, 4, 5, 6, 7
    # deque transforma esses números em uma fila:
    # [1, 2, 3, 4, 5, 6, 7]


    descartadas = []
    # Cria uma lista vazia.
    # Nela vamos guardar as cartas que forem descartadas.


    while len(fila) > 1:
        # len(fila) → quantidade de cartas que ainda estão na fila.
        # Enquanto houver MAIS DE UMA carta,
        # continuamos o processo.


        descartadas.append(str(fila.popleft()))
        # popleft() → RETIRA a primeira carta da fila.
        # Exemplo:
        # fila = [1, 2, 3, 4]
        # popleft() retira o 1:
        # fila = [2, 3, 4]
        # str() → transforma o número em texto.
        # append() → adiciona esse texto na lista descartadas.


        fila.append(fila.popleft())
        # Primeiro:
        # fila.popleft()
        # → retira a primeira carta da fila.
        # Depois:
        # fila.append(...)
        # → coloca essa carta no FINAL da fila.
        # Exemplo:
        # fila = [2, 3, 4]
        # popleft() → tira o 2
        # fila fica:
        # [3, 4]
        # append(2) → coloca o 2 no final
        # fila fica:
        # [3, 4, 2]


    # Quando o while termina,
    # significa que sobrou apenas UMA carta.


    print("Discarded cards", ", ".join(descartadas))
    # join() junta todos os elementos da lista
    # usando ", " como separador.
    # Exemplo:
    # descartadas = ["1", "3", "5"]
    # ", ".join(descartadas)
    # vira:
    # "1, 3, 5"


    print("Remaining card:", fila[0])
    # fila[0] pega o primeiro elemento da fila.
    # Como só existe uma carta,
    # fila[0] é a carta que restou.