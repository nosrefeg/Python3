zeroAVinte = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
              'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite número entre 0 e 20: '))
    while numero < 0 or numero > 20:
        print('Número não está na lista, tente novamente!')
        numero = int(input('Digite número entre 0 e 20: '))
    print(f'Você digitou o número {zeroAVinte[numero]}!')
    continuar = input('Você quer continuar? (S/N) ')
    while continuar not in 'SsNn':
        continuar = input('Você quer continuar? (S/N) ')
    if continuar in 'Nn':
        break
