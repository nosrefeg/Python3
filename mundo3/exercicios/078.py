valores = []
for i in range(0, 5):
    valores.append(int(input('Digite um número: ')))

print(f'''Você digitou os valores {valores}
O maior valor foi {max(valores)} nas posições ''', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i} ', end='')

print(
    f'\nO menor valor foi {min(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i} ', end='')
