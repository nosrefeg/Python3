num = soma = i = 0
while True:
    num = int(input('Digite um número inteiro (999 para parar): '))
    if num == 999:
        break
    soma += num
    i += 1
print(f'O total de números digitados é {i} e a soma entre eles é {soma}')
