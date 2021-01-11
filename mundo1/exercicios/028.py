import math
import random

numeroUsuario = int(input('Tente acertar o valor sorteado(entre 0 e 10): '))
numeroAle = random.randint(0, 10)
if numeroAle == numeroUsuario:
    print('Você acertou e venceu o jogo!!')
else:
    print('Você errou e perdeu o jogo!!')
print('FIM DE JOGO, O NÚMERO ERA: {}'.format(numeroAle))
