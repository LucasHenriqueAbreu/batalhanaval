
def cria_tabuleiro():
    tabuleiro = []
    for i in range(0, 10):
        linha = []
        for j in range(0, 10):
            linha.append(None)
        tabuleiro.append(linha)

    return tabuleiro