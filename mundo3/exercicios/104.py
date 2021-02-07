def leiaInt(msg):
    numero = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            numero = int(n)
            break
        else:
            print('\033[0;32mERRO! Digite um número inteiro válido!\033[m')

    return numero


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
