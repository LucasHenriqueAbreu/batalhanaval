from random import randint

def cria_jogador(id):
    nome = input('Informe o seu nome: ')
    return {
        'id': id,
        'nome': nome,
        'pontos': 0,
        'vez': False
    }


def placar(jogador1, jogador2):
    print('==== Placar ====')
    nomej1, pontosj1, nomej2, pontosj2 = jogador1.get('nome'), jogador1.get('pontos'), \
                                         jogador2.get('nome'), jogador2.get('pontos')
    print(f'{nomej1} está com {pontosj1} pontos e {nomej2} está com {pontosj2} pontos')
    nome_jogador_da_vez = jogador1.get('nome') if jogador1.get('vez') else jogador2.get('nome')
    print(f'A vez de jogar é de {nome_jogador_da_vez}')


def sortear_jogador_inicial(jogador1, jogador2):
    jogadores = jogador1, jogador2
    numero_sorteado = randint(0, 1)
    jogadores[numero_sorteado]['vez'] = True
    return jogadores
