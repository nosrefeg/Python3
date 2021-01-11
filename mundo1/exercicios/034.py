salario = float(input('Digite o valor do seu salário: '))
if salario <= 1250:
    print('Seu aumento é de R${}'.format((salario * 15)/100))
else:
    print('Seu aumento é de R${}'.format((salario * 10)/100))
