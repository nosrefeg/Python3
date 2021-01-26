jogador = {
    'nome': input('Nome do jogador: '),
    'gols': []
}

partidas = int(input('Quantas partidas ele jogou? '))
for i in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i + 1}? ')))
jogador['total'] = sum(jogador['gols'])

print('--' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('--' * 30)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i in range(0, len(jogador['gols'])):
    print(f'    --> Na partida {i + 1} ele fez {jogador["gols"][i]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
