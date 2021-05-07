
def pedir_nome(id):
    return input('Informe o seu nome: ')


def placar(jogador1, jogador2):
    print('==== Placar ====')
    nomej1, pontosj1, nomej2, pontosj2 = jogador1.get('nome'), jogador1.get('pontos'), \
                                         jogador2.get('nome'), jogador2.get('pontos')
    print(f'{nomej1} está com {pontosj1} pontos e {nomej2} está com {pontosj2} pontos')
    nome_jogador_da_vez = jogador1.get('nome') if jogador1.get('vez') else jogador2.get('nome')
    print(f'A vez de jogar é de {nome_jogador_da_vez}')


