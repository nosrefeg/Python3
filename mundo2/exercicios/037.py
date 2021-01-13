numero = int(input('Digite um número inteiro: '))
opcao = int(input('''Selecione a base de conversão:
1 para Binário
2 para octal
3 para hexadecimal
'''))

if opcao == 1:
    print('{} convertido para binário é: {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para octal é: {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é: {}'.format(
        numero, hex(numero)[2:]))
else:
    print('Opção inválida')
