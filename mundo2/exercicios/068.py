import random
i = num = parim = soma = win = 0
pc = random.randint(0, 10)
while True:
    print('JOGO DE PAR OU ÍMPAR')
    num = int(input('Digite um número (maior que 10 para parar): '))
    parim = input('Par ou Ímpar? (P/I) ').strip().upper()
    i += 1
    soma = num + pc
    if soma % 2 == 0 and parim == 'P':
        print(f'\nVocê jogou {num} e o computador {pc}, total de {soma}')
        print('VOCÊ VENCEU\n')
        win += 1
    elif soma % 2 == 1 and parim == 'I':
        print(f'\nVocê jogou {num} e o computador {pc}, total de {soma}')
        print('VOCÊ VENCEU\n')
        win += 1
    else:
        print(f'\nVocê jogou {num} e o computador {pc}, total de {soma}')
        print('O COMPUTADOR VENCEU\n')
        break
print(f'Você venceu {win} de {i} tentativas!')
