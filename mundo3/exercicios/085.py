valores = [[], []]
for i in range(0, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        valores[0].append(numero)
    if numero % 2 == 1:
        valores[1].append(numero)
print('¨¨' * 30)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
