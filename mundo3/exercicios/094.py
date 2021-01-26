listaPessoas = []
listaMulher = []
somaIdade = 0
while True:
    pessoa = {
        'nome': input('Nome: '),
        'sexo': input('Sexo: (F/M) ').strip().upper(),
        'idade': int(input('Idade: '))
    }
    somaIdade += pessoa['idade']
    if pessoa['sexo'] == 'F':
        listaMulher.append(pessoa['nome'])

    listaPessoas.append(pessoa)

    cont = input('Quer continuar: (S/N) ').strip().upper()
    if cont == 'N':
        break

mediaIdade = somaIdade / len(listaPessoas)
acimaMedia = []
print('--' * 30)
print(f'Foram cadastradas {len(listaPessoas)} pessoas!')
print(f'A média de idade do grupo é {mediaIdade} anos')
print(f'As mulheres do grupo são {listaMulher}')
for i in range(0, len(listaPessoas)):
    if listaPessoas[i]['idade'] > mediaIdade:
        acimaMedia.append(listaPessoas[i]['nome'])
print(f'As pessoas acima da média de idade são {acimaMedia}')
