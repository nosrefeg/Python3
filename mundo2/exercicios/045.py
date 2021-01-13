import random
jogador = input('Digite pedra, papel ou tesoura: ').strip().lower()
pc = random.choice(['pedra', 'papel', 'tesoura'])

if jogador == 'pedra' and pc == 'pedra':
    print('Vocês empataram!')
elif jogador == 'pedra' and pc == 'papel':
    print('Você perdeu!')
elif jogador == 'pedra' and pc == 'tesoura':
    print('Você ganhou!')
elif jogador == 'papel' and pc == 'pedra':
    print('Você ganhou!')
elif jogador == 'papel' and pc == 'papel':
    print('Vocês empataram!')
elif jogador == 'papel' and pc == 'tesoura':
    print('Você perdeu!')
elif jogador == 'tesoura' and pc == 'pedra':
    print('Vocês perdeu!')
elif jogador == 'tesoura' and pc == 'papel':
    print('Você ganhou!')
elif jogador == 'tesoura' and pc == 'tesoura':
    print('Vocês empataram!')
