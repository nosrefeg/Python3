valores = (int(input('Digite um número: ')), int(input('Digite mais um número: ')), int(
    input('Digite mais um número: ')), int(input('Digite mais um número: ')))

print(
    f'Você digitou os valores {valores} \nO valor 9 apareceu {valores.count(9)} vezes')

if valores.index(3):
    print(f'O número três foi digitado na {valores.index(3) + 1}ª posição')
else:
    print(f'O número três não foi digitado em nenhuma posição')

print('Os valores pares foram: ', end='')

for i in valores:
    if i % 2 == 0:
        print(i, end=' ')

# numNove = numPar = 0
# for i in range(0, 4):
#     if valores[i] == 9:
#         numNove += 1
#     if valores[i] % 2 == 0:
#         numPar += 1
