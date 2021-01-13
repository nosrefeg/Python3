sexo = 'a'
while sexo not in 'MF':
    sexo = input('Digite seu sexo (F/M): ').upper()
    if sexo not in 'MF':
        print('Valor inexistente, digite novamente!')
print('Muito bem!')

# sexo = ' '
# mulher = 0
# homem = 0
# while sexo != '0':
#     sexo = input('''Digite seu sexo: (F/M)
# 0 para finalizar\n''').upper()
#     if sexo == 'F':
#         mulher += 1
#     elif sexo == 'M':
#         homem += 1
#     else:
#         print('Valor incorreto, tente novamente ou finalize o programa!')
# print('{} mulheres e {} homens'.format(mulher, homem))
