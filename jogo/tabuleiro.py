
def cria_tabuleiro(jogador):
    tabuleiro = {
        'jogador': jogador,
        'area': []
    }
    for i in range(0, 10):
        linha = []
        for j in range(0, 10):
            linha.append(None)
        tabuleiro['area'].append(linha)

    return tabuleiro