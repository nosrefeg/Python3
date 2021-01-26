from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
ranking = []

print('Valores Sorteados: ')
for i in range(0, 4):
    jogadores[f'jogador{i+1}'] = randint(1, 6)
    print(f'    O {f"jogador{i+1}"} tirou {jogadores[f"jogador{i+1}"]}')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('\nRanking: ')
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
