nome = input('Digite seu nome completo: ')
nArray = nome.split()
tamanho = nArray.__len__()
print('''Primeiro nome: {}
Segundo nome: {}'''.format(nArray[0], nArray[tamanho-1]))
