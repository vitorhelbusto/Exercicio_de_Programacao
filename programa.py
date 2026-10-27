from funcoes import posicao_valida, preenche_frota, posiciona_frota, monta_tabuleiros, faz_jogada, afundados
from random import randint
qnt_tamanhos = {
    "porta-aviões":[1, 4],
    "navio-tanque":[2, 3],
    "contratorpedeiro":[3, 2],
    "submarino": [4, 1],
} 

frota = {}

for nome,info in qnt_tamanhos.items():
    for i in range(info[0]):
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {info[1]}')
        if nome == 'submarino':
            linha = int(input('linha:'))
            coluna = int(input('coluna:'))
            orientacao = 'vertical'
        else:
            linha = int(input('linha:'))
            coluna = int(input('coluna:'))
            orientacao = int(input('orientacao:'))
            if orientacao == 1:
                orientacao = 'vertical'
            elif orientacao == 2:
                orientacao = 'horizontal'
        while posicao_valida(frota, linha, coluna, orientacao, info[1]) == False:
            print('Esta posição não está válida!')
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho {info[1]}')
            if nome == 'submarino':
                linha = int(input('linha:'))
                coluna = int(input('coluna:'))
                orientacao = 'vertical'
            else:
                linha = int(input('linha:'))
                coluna = int(input('coluna:'))
                orientacao = int(input('orientacao:'))
                if orientacao == 1:
                    orientacao = 'vertical'
                elif orientacao == 2:
                    orientacao = 'horizontal'
        
        frota = preenche_frota(frota, nome, linha, coluna, orientacao, info[1])

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

quantidade_navios = 0
quantidade_navios_oponente = 0
for j in frota_oponente:
    quantidade_navios += len(frota_oponente[j])

for l in frota:
    quantidade_navios_oponente += len(frota[l])


tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)
historico_jogadas = []
historico_jogadas_oponente = []

jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    while True:
        linha = int(input('Jogador, qual linha deseja atacar?'))
        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Jogador, qual linha deseja atacar?'))
        coluna = int(input('Jogador, qual coluna deseja atacar?'))
        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Jogador, qual coluna deseja atacar?'))

        posicao = [linha, coluna]
        if posicao in historico_jogadas:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
            continue

        break
    
    historico_jogadas.append(posicao)

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == quantidade_navios:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    else:
        linha_oponente = randint(0,9)
        coluna_oponente = randint(0,9)
        posicao_oponente = [linha_oponente, coluna_oponente]
        while posicao_oponente in historico_jogadas_oponente:
            linha_oponente = randint(0,9)
            coluna_oponente = randint(0,9)
            posicao_oponente = [linha_oponente, coluna_oponente]
        historico_jogadas_oponente.append(posicao_oponente)
        print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}')
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)

        if afundados(frota, tabuleiro_jogador) == quantidade_navios_oponente:
                print('Xi! O oponente derrubou toda a sua frota =(')
                jogando = False

            
        


