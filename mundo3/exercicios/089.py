alunos = []

while True:
    dados = [input('Digite o nome do aluno: '), [float(
        input('Digite a primeira nota: ')), float(input('Digite a segunda nota: '))]]
    alunos.append(dados[:])

    confirm = input('Quer continuar? (S/N) ').strip().upper()
    while confirm not in 'SN':
        confirm = input('Quer continuar? (S/N) ').strip().upper()
    if confirm == 'N':
        print('==' * 30)
        print(f'{"Nº":<5} {"Nome":^5} {"Média":>10}')
        print('--' * 30)
        for i in range(0, len(alunos)):
            print(
                f'{i:<5} {alunos[i][0]:^5} {(alunos[i][1][0] + alunos[i][1][1]) / 2:>10}')
        print('--' * 30)
        while True:
            pos = int(input('Mostrar notas de qual aluno? (999 para parar) '))
            if pos == 999:
                break
            if pos < len(alunos):
                print(f'Notas de {alunos[pos][0]} são {alunos[pos][1]}')
        break
