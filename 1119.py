# Continua lendo casos até encontrar 0 0 0
while True:

    # Lê três números:
    # n = quantidade de pessoas
    # k = posição/contagem feita no sentido horário
    # m = posição/contagem feita no sentido contrário
    n, k, m = map(int, input().split())


    # Se os três forem 0, termina o programa
    if n == 0 and k == 0 and m == 0:
        break


    # Cria a lista de pessoas
    # Exemplo: se n = 5 → [1, 2, 3, 4, 5]
    pessoas = list(range(1, n + 1))


    # Cria uma lista dizendo quais pessoas ainda estão ativas
    # True  = pessoa ainda está no jogo
    # False = pessoa já foi eliminada
    #
    # Exemplo com n = 5:
    # [True, True, True, True, True]
    ativas = [True] * n


    # Posição inicial da contagem de k
    # Começa na primeira pessoa
    pos_k = 0


    # Posição inicial da contagem de m
    # Começa na última pessoa
    pos_m = n - 1


    # Quantidade de pessoas que já foram eliminadas
    quantidade = 0


    # Lista que vai guardar a resposta final
    resultado = []


    # Continua enquanto ainda houver pessoas para eliminar
    while quantidade < n:


        # Começa a contagem de k
        contador = k


        # Repete até terminar a contagem
        while contador > 0:

            # Verifica se a pessoa atual ainda está ativa
            if ativas[pos_k]:

                # Se estiver ativa, conta essa pessoa
                contador -= 1


            # Se ainda não terminou a contagem,
            # passa para a próxima posição
            if contador > 0:
                pos_k = (pos_k + 1) % n


        # Guarda o número da pessoa escolhida por k
        pessoa_k = pessoas[pos_k]


        # Começa a contagem de m
        contador = m


        # Repete até terminar a contagem
        while contador > 0:

            # Verifica se a pessoa atual ainda está ativa
            if ativas[pos_m]:

                # Se estiver ativa, conta
                contador -= 1


            # Se ainda não terminou,
            # volta uma posição
            if contador > 0:
                pos_m = (pos_m - 1) % n


        # Guarda o número da pessoa escolhida por m
        pessoa_m = pessoas[pos_m]


        # Verifica se os dois escolheram a mesma pessoa
        if pessoa_k == pessoa_m:

            # Coloca essa pessoa no resultado
            resultado.append(str(pessoa_k))

            # Marca a pessoa como eliminada
            ativas[pos_k] = False

            # Aumenta a quantidade de eliminados
            quantidade += 1


        # Caso k e m tenham escolhido pessoas diferentes
        else:

            # Adiciona a pessoa escolhida por k
            resultado.append(str(pessoa_k))

            # Adiciona a pessoa escolhida por m
            resultado.append(str(pessoa_m))

            # Elimina a pessoa escolhida por k
            ativas[pos_k] = False

            # Elimina a pessoa escolhida por m
            ativas[pos_m] = False

            # Foram eliminadas duas pessoas
            quantidade += 2


        # Depois da eliminação,
        # passa a posição de k para a próxima pessoa
        pos_k = (pos_k + 1) % n

        # E passa a posição de m para a pessoa anterior
        pos_m = (pos_m - 1) % n


    # Junta os resultados colocando ", " entre eles
    print(", ".join(resultado))