media = 0
idades = 0
mm20 = 0
hmaisvelho = 0
nomevelho = 0
for i in range(0, 4):
    print('------ {} pessoa ------'.format(i+1))
    nome = input('Digite seu nome: ')
    sexo = input('Digite seu sexo(M ou F): ').upper()
    idade = int(input('Digite sua idade: '))
    idades += idade
    media = idades / 4
    if sexo == 'F' and idade < 20:
        mm20 += 1
    if sexo == 'M' and i == 0:
        hmaisvelho = idade
        nomevelho = nome
    if sexo == 'M' and idade > hmaisvelho:
        hmaisvelho = idade
        nomevelho = nome
print('A média das idade é {}, com {} mulheres abaixo de 20 anos e o homem mais velho é {}'.format(
    media, mm20, nomevelho))
