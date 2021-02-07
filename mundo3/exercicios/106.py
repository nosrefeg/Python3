from time import sleep


def ajuda(comando):
    print('\033[0;30;43m^^\033[m' * 20)
    print(
        f'\033[0;30;43m{f"Acessando o manual do comando {comando}":^30}\033[m')
    print('\033[0;30;43m^^\033[m' * 20)
    sleep(1)
    return help(comando)


while True:
    print('\033[0;30;45m^^\033[m' * 15)
    print(f'\033[0;30;45m{"SISTEMA DE AJUDA PYHELP":^30}\033[m')
    print('\033[0;30;45m^^\033[m' * 15)
    sleep(1)
    comando = input(
        'Digite o comando ou biblioteca para ver o manual (fim para sair): ').lower().strip()
    if comando.upper() == 'FIM':
        sleep(1)
        print('\033[0;30;42m^^\033[m' * 10)
        print(
            f'\033[0;30;42m{"ATÉ LOGO!":^20}\033[m')
        print('\033[0;30;42m^^\033[m' * 10)
        break
    ajuda(comando)
