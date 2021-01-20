matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = num = int(
            input(f'Digite um valor para a posição [{l}][{c}]: '))

print('¨¨' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[  {matriz[l][c]:^4}  ]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()

tColum = matriz[0][2] + matriz[1][2] + matriz[2][2]
print('¨¨' * 30)
print(f'A soma de todos os valores pares é {pares}')
print(
    f'A soma dos valores da terceira coluna é {tColum}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

# matriz = [[[], [], []], [[], [], []], [[], [], []]]
# pares = 0
# for i in range(0, 3):
#     num = int(input('Digite um valor para a matriz: '))
#     if num % 2 == 0:
#         pares += num
#     if 0 <= i <= 2:
#         matriz[0][i] = num

# for i in range(0, 3):
#     num = int(input('Digite um valor para a matriz: '))
#     if num % 2 == 0:
#         pares += num
#     if 0 <= i <= 2:
#         matriz[1][i] = num

# for i in range(0, 3):
#     num = int(input('Digite um valor para a matriz: '))
#     if num % 2 == 0:
#         pares += num
#     if 0 <= i <= 2:
#         matriz[2][i] = num

# print('¨¨' * 30)
# for i in range(0, 3):
#     print(f'[  {matriz[0][i]}  ]', end='')
# print('')
# for i in range(0, 3):
#     print(f'[  {matriz[1][i]}  ]', end='')
# print('')
# for i in range(0, 3):
#     print(f'[  {matriz[2][i]}  ]', end='')
# print('')
# print('¨¨' * 30)
# print(f'A soma de todos os valores pares é {pares}')
# print(
#     f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
# print(f'O maior valor da segunda linha é {max(matriz[1])}')
