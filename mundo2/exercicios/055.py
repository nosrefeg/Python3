maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso foi {} e o menor foi {}'.format(maior, menor))
