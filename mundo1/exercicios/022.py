nomeCompleto = input('Digite seu nome completo: ')
print('Em maiusculo: {}'.format(nomeCompleto.upper()))
print('Em minusculo: {}'.format(nomeCompleto.lower()))
print('Total de letras no nome : {}'.format(
    len(nomeCompleto.replace(' ', ''))))
nomeArray = nomeCompleto.split()
print('Primeiro nome: {}'.format(nomeArray[0]))
print('Total de letras no primeiro nome: {}'.format(len(nomeArray[0])))
