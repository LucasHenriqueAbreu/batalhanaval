
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

def posicionar_barcos(tabuleiros, jogadores):
    resultado_tabuleiros = []
    for jogador in jogadores:
        print(f'Jogador {jogador.get("nome")}, é sua vez de posicionar os barcos!')
        print('Antenção: Peça para seu adversário não olhar seu posicionamento.')
        tabuleiro = busca_tabuleiro_por_jogador(jogador, tabuleiros)
        for i in range(0, 5):
            indice_linha = int(input(f'Qual linha deseja colocar o seu {i + 1}° barco?'))
            indice_coluna = int(input(f'Qual coluna deseja colocar o seu {i + 1}° barco?'))
            tabuleiro.get('area')[indice_linha][indice_coluna] = ' B '

        resultado_tabuleiros.append(tabuleiro)

    return resultado_tabuleiros


def busca_tabuleiro_por_jogador(jogador, tabuleiros):
    for tabuleiro in tabuleiros:
        if tabuleiro.get('jogador').get('id') == jogador.get('id'):
            return tabuleiro