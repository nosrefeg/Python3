idade = m18 = homens = mm20 = sexo = go = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo (M/F): ').strip().upper()
    while sexo not in 'MF':
        sexo = input('Digite seu sexo (M/F): ').strip().upper()
    if idade > 18:
        m18 += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mm20 += 1
    go = input('Quer continuar? (S/N) ').strip().upper()
    while go not in 'SN':
        go = input('Quer continuar? (S/N) ').strip().upper()
    if go == 'N':
        break
print(
    f'Foram cadastradas: \n{m18} com mais de 18 anos \n{homens} homens \n{mm20} mulheres com menos de 20 anos!')
