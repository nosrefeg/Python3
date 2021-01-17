numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))
    continua = input('Quer continuar? (S/N) ').strip().upper()
    while continua not in 'SN':
        print('Apenas S ou N')
        continua = input('Quer continuar? (S/N) ').strip().upper()
    if continua == 'N':
        break
print('¨¨' * 30)
print(f'Foram digitados {len(numeros)} números!')
numeros.sort(reverse=True)
print(f'Os números de forma decrescente são {numeros}')

if 5 in numeros:
    print(f'O número 5 está na lista, na {numeros.index(5) + 1}ª posição')

else:
    print('O número 5 NÃO está na lista!')
