soma = 0
for i in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
print('O total é: {}'.format(soma))
