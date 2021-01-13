preco = float(input('Digite o preço do produto: '))
tipo = int(input('''Digite o número do tipo de pagamento:
 à vista no dinheiro/cheque: 1
 à vista no cartão: 2
 2x no cartão: 3
 3x ou mais no cartão: 4
 Opção: '''))

if tipo == 1:
    print('\n O valor final foi {}'.format(preco - (preco * 10)/100))
elif tipo == 2:
    print('\n O valor final foi {}'.format(preco - (preco * 5)/100))
elif tipo == 3:
    print('\n O valor final foi {}'.format(preco))
elif tipo == 4:
    print('\n O valor final foi {}'.format(preco + (preco * 20)/100))
else:
    print('Opção inválida!')
