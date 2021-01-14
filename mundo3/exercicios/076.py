lista = ('café', 5.50, 'doce', 13, 'caderno', 22, 'notebook', 4.500)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R${lista[i]:>8.2f}')
print('-' * 40)
