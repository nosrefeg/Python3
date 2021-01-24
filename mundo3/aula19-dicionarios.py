pessoas = {
    'nome': 'Moral',
    'language': 'PT-BR'
}
print(pessoas)
print('--' * 10)
pessoas['idade'] = 21
print(pessoas)
print('--' * 10)
print(pessoas.values())
print('--' * 10)
print(pessoas.keys())
print('--' * 10)
print(pessoas.items())
print('--' * 10)
for k, v in pessoas.items():
    print(f'{k} é {v}')
print('--' * 10)
print(type(pessoas))
print('--' * 10)
estado = {}
br = []
for i in range(0, 3):
    estado['nome'] = input('Nome do seu estado: ')
    estado['sigla'] = input('sigla do seu estado: ')
    br.append(estado.copy())

print(br)
print('--' * 10)
