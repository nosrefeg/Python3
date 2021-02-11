import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p, True)}')
print(f'O dobro de {p} é {moeda.dobro(p, False)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 16%, temos {moeda.diminuir(p, 16, False)}')
