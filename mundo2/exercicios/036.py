casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite em quantos anos quer pagar: '))
parcela = casa/anos
porcento = (salario * 30)/100

if parcela > porcento:
    print('Infelizmente seu empréstimo foi negado!')
else:
    print('Seu empréstimo foi aceito!')
