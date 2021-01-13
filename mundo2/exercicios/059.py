num1 = num2 = opcao = 0
while opcao != 5:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
    opcao = int(input('''Escolha uma opção:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR
        '''))
    if opcao == 1:
        print('A soma dos números {} e {} é {}'.format(num1, num2, num1 + num2))
        opcao = int(input('''Escolha uma opção:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR
        '''))
    if opcao == 2:
        print('A multiplicação dos números {} e {} é {}'.format(
            num1, num2, num1 * num2))
        opcao = int(input('''Escolha uma opção:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR
        '''))
    if opcao == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num1 < num2:
            print('{} é maior que {}'.format(num2, num1))
        else:
            print('Os dois números são iguais!')
        opcao = int(input('''Escolha uma opção:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR
        '''))
