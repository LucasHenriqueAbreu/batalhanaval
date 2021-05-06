from random import randint

def cria_jogador():
    nome = input('Informe o seu nome: ')
    return {
        'nome': nome,
        'pontos': 0,
        'vez': False
    }


def placar(jogador1, jogador2):
    print('==== Placar ====')
    print('{0} está com {1} pontos e {2} está com {3} pontos'.format(
        jogador1.get('nome'), jogador1.get('pontos'), jogador2.get('nome'), jogador2.get('pontos')
    ))
    nome_jogador_da_vez = jogador1.get('nome') if jogador1.get('vez') else jogador2.get('nome')
    print('A vez de jogar é de {}'.format(nome_jogador_da_vez))


def sortear_jogador_inicial(jogador1, jogador2):
    jogadores = jogador1, jogador2
    numero_sorteado = randint(0, 1)
    jogadores[numero_sorteado]['vez'] = True
    return jogadores
