def ficha(nome='', gols=0):
    if nome == '':
        return f'O jogador <desconhecido> fez {gols} gol(s) no campeonato'
    else:
        return f'O jogador {nome} fez {gols} gol(s) no campeonato'


print('--' * 30)
nome = input('Nome do jogador: ').strip()
gols = input('Quantos gols ele fez? ')
if gols == '' or gols.isalpha() == True:
    gols = 0
else:
    int(gols)
print(ficha(nome, gols))
