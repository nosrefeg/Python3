num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

if num1 > num2:
    print('{} é maior'.format(num1))
elif num2 > num1:
    print('{} é maior'.format(num2))
elif num1 == num2:
    print('Os dos valores são iguais!!')
