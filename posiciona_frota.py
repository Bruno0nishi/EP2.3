def posiciona_frota(frota):
    tabuleiro = [[0]*10 for _ in range(10)]
    for tipo_navio, posicoes in frota.items():
        for posicao in posicoes:
            for x, y in posicao:
                tabuleiro[x][y] = 1
    return tabuleiro

    #cria um tabuleiro de 10x10 usando uma lista
    #A variável "_" é usada como um espaço reservado para a variável de loop
