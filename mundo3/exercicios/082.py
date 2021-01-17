numPares = []
numImpares = []
numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))
    continua = input('Quer continuar? (S/N) ').strip().upper()
    while continua not in 'SN':
        print('Apenas S ou N')
        continua = input('Quer continuar? (S/N) ').strip().upper()
    if continua == 'N':
        break
for i in numeros:
    if i % 2 == 0:
        numPares.append(i)
    else:
        numImpares.append(i)

numeros.sort()
numPares.sort()
numImpares.sort(reverse=True)

print('~~' * 32)
print(f'Todos os números digitados, em ordem crescente, foram: {numeros}')
print(f'Os números pares digitados, em ordem crescente foram: {numPares}')
print(
    f'Os números ímpares digitados, em ordem decrescente foram: {numImpares}')
