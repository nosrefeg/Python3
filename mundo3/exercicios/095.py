listaJogadores = []
while True:
    jogador = {
        'nome': input('Nome do jogador: '),
        'gols': []
    }

    partidas = int(input('Quantas partidas ele jogou? '))
    for i in range(0, partidas):
        jogador['gols'].append(
            int(input(f'    Quantos gols na partida {i + 1}? ')))
    jogador['total'] = sum(jogador['gols'])

    listaJogadores.append(jogador)
    cont = input('Quer continuar? (S/N) ').strip().upper()
    if cont == 'N':
        print('==' * 30)
        print(f'{"Cod":<5} {"Nome":<5} {"Gols":^10} {"Total":>15}')
        print('--' * 30)
        for i in range(0, len(listaJogadores)):
            print(
                f'{i:<5} {listaJogadores[i]["nome"]:<5} {str(listaJogadores[i]["gols"]):<10} {listaJogadores[i]["total"]:>15}')
        print('--' * 30)
        while True:
            escolha = int(
                input('Mostrar dados de qual jogar? (pelo código)(999 para parar) '))

            if escolha == 999:
                break
            if escolha <= len(listaJogadores):
                print('--' * 30)
                print(
                    f'-* LEVANTAMENTO DO JOGADOR {listaJogadores[escolha]["nome"]} *-')
                for i in range(0, len(listaJogadores[escolha]["gols"])):
                    print(
                        f'    No jogo {i + 1} fez {listaJogadores[escolha]["gols"][i]} gols')
                print(f'  Um total de {jogador["total"]} gols')
                print('--' * 30)
            else:
                print(
                    f'ERRO!!! Não existe jogador com o código {escolha} cadastrado! Tente novamente!')
        break
print('VOLTE SEMPRE!')
