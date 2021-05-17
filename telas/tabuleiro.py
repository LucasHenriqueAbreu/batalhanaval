from time import sleep

from utils.fonte_cor import adiciona_cor


def mostrar_tabuleiro(tabuleiros):
    for i, tabuleiro in enumerate(tabuleiros):
        id_jogador = tabuleiro['jogador']['id']
        area = tabuleiro['area']
        for j, linha in enumerate(area):
            if j == 0 and id_jogador == 1:
                mostrar_indice_coluna(len(linha))
            mostrar_indice_linha(j)
            for posicao in linha:
                cor = '31m' if id_jogador == 1 else '34m'
                valor = posicao or ' * '
                print(f'{adiciona_cor(cor, valor)}', end=' ')
            print()
            if j == len(area) - 1 and id_jogador == 2:
                mostrar_indice_coluna(len(linha))
            sleep(0.05)
        if i == 0:
            print(' = ' * 13)


def mostrar_indice_coluna(tamanho_linha):
    for count in range(0, tamanho_linha):
        end = '\n' if count == tamanho_linha - 1 else ' '
        espaco_extra = '  ' if count == 0 else ''
        print(f'{espaco_extra} {adiciona_cor("33m", count)} ', end=end)


def mostrar_indice_linha(indice):
    print(adiciona_cor("33m", indice), end=':')

