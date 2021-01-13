numero = maior = menor = soma = c = 0
opcao = ''
i = 1
while i != 0:
    numero = int(input('Digite um número inteiro: '))
    c += 1
    soma += numero
    if i == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        else:
            menor = numero
    i += 1
    opcao = str(input('Quer continuar a digitar? (S/N): ')).strip().upper()
    if opcao == 'N':
        i = 0
print('A soma de todos os valores é {} e a média entre eles é {}, com {} sendo o maior e {} o menor!'.format(
    soma, soma/c, maior, menor))
