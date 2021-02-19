# Exercício 104 melhorado. com tratamento de erros e uma função a mais


def leiaInt(msg):
    numero = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            numero = int(n)
            break
        else:
            print('\033[0;32mERRO! Digite um número inteiro válido!\033[m')

    return numero


def leiaReal(msg):
    numero = 0
    while True:
        n = str(input(msg)).strip()
        if n.find('.') != -1 and n.replace('.', '').isnumeric():
            numero = float(n)
            break
        else:
            print('\033[0;32mERRO! Digite um número real válido!\033[m')

    return numero


inteiro = real = 0

try:
    inteiro = leiaInt('Digite um número inteiro: ')
except KeyboardInterrupt as erro:
    inteiro = 0
    print('\033[0;32m\nO usuário preferiu não digitar esse valor!\033[m')

try:
    real = leiaReal('Digite um número real: ')
except KeyboardInterrupt as erro:
    real = 0
    print('\033[0;32m\nO usuário preferiu não digitar esse valor!\033[m')
finally:
    print(
        f'\033[1mO número inteiro foi {inteiro} e o número real {real}\033[m')
