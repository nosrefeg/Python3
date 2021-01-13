import random
pc = random.randint(0, 10)
player = 11
tentativas = 0
print('-------- JOGO DA ADIVINHAÇÃO -------')
while pc != player:
    player = int(input('Tente adivinhar o número certo: '))
    tentativas += 1
print('''Você acertou, parabéns!!
E precisou de {} tentativas'''.format(tentativas))
