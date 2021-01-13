from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print('Você ainda vai se alistar, faltam ({}) anos!'.format(18 - idade))
elif idade == 18:
    print('Você deve se alistar!')
else:
    print('Passou da idade de alistamento, com atraso de ({}) anos!'.format(idade - 18))
