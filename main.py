from jogo.jogadores import criar_jogadores, sortear_jogador_inicial
from jogo.tabuleiro import cria_tabuleiro
from telas.jogadores import placar
from telas.mensagens import mensagem_inicializacao
from telas.tabuleiro import mostrar_tabuleiro


def rodar_programa():
    mensagem_inicializacao()
    jogador1, jogador2 = criar_jogadores()
    jogador1, jogador2 = sortear_jogador_inicial(jogador1, jogador2)
    placar(jogador1, jogador2)
    tabuleiros = cria_tabuleiro(jogador1), cria_tabuleiro(jogador2)
    mostrar_tabuleiro(tabuleiros)
    # Posicionamento dos barcos
    # Batalha, ou seja, jogadores atirando um no outro até que um seja derrotado!
    # mostra o vencedor

rodar_programa()
