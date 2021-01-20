from random import randint
from time import sleep

mega = []
jogos = []

print(f'--' * 30)
print(f'{"JOGO DA MEGA SENA":^60}')
print(f'--' * 30)
print('')
qtdJogos = int(input('Quantos jogos deseja fazer? '))
total = 1
while total <= qtdJogos:
    i = 0
    while True:
        numero = randint(1, 60)
        if numero not in jogos:
            jogos.append(numero)
            i += 1
        if i >= 6:
            break
    jogos.sort()
    mega.append(jogos[:])
    total += 1
print(f'{" SORTEANDO SEUS JOGOS ":$^60}')
for i in range(0, qtdJogos):
    print(f'Seu jogo número {i + 1} é: {mega[i]}')
    sleep(1)
print(f'{" BOA SORTE ":$^60}')
# Minha primeira solução

# from random import randint
# from time import sleep

# mega = []

# print(f'--' * 30)
# print(f'{"JOGO DA MEGA SENA":^60}')
# print(f'--' * 30)
# print('')
# jogos = int(input('Quantos jogos deseja fazer? '))
# print(f'{" SORTEANDO SEUS JOGOS ":$^60}')

# for i in range(0, jogos):
#     jogoFeito = [randint(0, 60), randint(0, 60), randint(
#         0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]
#     jogoFeito.sort()
#     mega.append(jogoFeito[:])
#     print(f'Seu jogo número {i + 1} é: {mega[i]}')
#     sleep(1)
# print(f'{" BOA SORTE ":$^60}')
