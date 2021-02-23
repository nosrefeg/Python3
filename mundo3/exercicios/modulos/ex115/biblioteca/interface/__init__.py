def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;32mERRO! Digite uma opção válida!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;32m\nO usuário preferiu não digitar!\033[m')
            return 3
        else:
            return n


def menu():
    print('-' * 50)
    print(f'{"MENU PRINCIPAL":^50}')
    print('-' * 50)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-' * 50)
    resposta = leiaInt('Sua opção: ')
    return resposta


def sair():
    print('-' * 50)
    print(f'{"Saindo do sistema. Até breve!":^50}')
    print('-' * 50)
