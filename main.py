from jogo.tabuleiro import cria_tabuleiro
from telas.jogadores import cria_jogador, placar, sortear_jogador_inicial
from telas.mensagens import mensagem_inicializacao, mensagem_criacao_jogador
from telas.tabuleiro import mostrar_tabuleiro


def criar_jogadores():
    mensagem_criacao_jogador('Jogador 1')
    jogador1 = cria_jogador()
    mensagem_criacao_jogador('Jogador 2')
    jogador2 = cria_jogador()
    return jogador1, jogador2

def rodar_programa():
    mensagem_inicializacao()
    jogador1, jogador2 = criar_jogadores()
    jogador1, jogador2 = sortear_jogador_inicial(jogador1, jogador2)
    placar(jogador1, jogador2)
    tabuleiro = cria_tabuleiro()
    mostrar_tabuleiro(tabuleiro)

rodar_programa()
