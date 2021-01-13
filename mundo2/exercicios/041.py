from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('CATEGORIA: MIRIM')
elif idade > 9 and idade <= 14:
    print('CATEGORIA: INFANTIL')
elif idade > 14 and idade <= 19:
    print('CATEGORIA: JUNIOR')
elif idade > 19 and idade <= 20:
    print('CATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')
