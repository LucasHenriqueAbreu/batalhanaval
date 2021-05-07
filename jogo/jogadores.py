from random import randint

from telas.jogadores import pedir_nome
from telas.mensagens import mensagem_criacao_jogador


def criar_jogadores():
    mensagem_criacao_jogador('Jogador 1')
    jogador1 = criar_jogador(1)
    mensagem_criacao_jogador('Jogador 2')
    jogador2 = criar_jogador(2)
    return jogador1, jogador2


def criar_jogador(id):
    nome = pedir_nome()
    return {
        'id': id,
        'nome': nome,
        'pontos': 0,
        'vez': False
    }

def sortear_jogador_inicial(jogador1, jogador2):
    jogadores = jogador1, jogador2
    numero_sorteado = randint(0, 1)
    jogadores[numero_sorteado]['vez'] = True
    return jogadores
