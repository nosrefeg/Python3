zeroAVinte = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
              'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite número entre 0 e 20: '))
while True:
    while numero < 0 or numero > 20:
        print('Número não está na lista, tente novamente!')
        numero = int(input('Digite número entre 0 e 20: '))
    print(f'Você digitou o número {zeroAVinte[numero]}!')
    break
