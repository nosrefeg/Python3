numero = int(input('Digite um número inteiro: '))
soma = 0
i = 0
while numero < 999:
    soma += numero
    i += 1
    numero = int(input('''Digite um número inteiro: 
    999 para parar\n'''))
print('A quantidade de números digitados foi {} e a soma entre eles foi de {}'.format(i, soma))
