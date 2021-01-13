frase = input('Digite uma frase: ').replace(' ', '')
inversa = ''
for i in range(len(frase) - 1, -1, -1):
    inversa += frase[i]
if inversa == frase:
    print('{} é um palíndromo!'.format(frase))
else:
    print('{} não é um palíndromo'.format(frase))

# sem for
# palin = frase[::-1]
# if palin == frase:
#     print('É um palíndromo!')
# else:
#     print('Não é um palíndromo')
