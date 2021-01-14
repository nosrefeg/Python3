brasileirao2018 = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos',
                   'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC', 'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')
print(
    f'Lista da série A do brasileirão de 2018: \n{brasileirao2018}', end='\n\n')
print('¨¨' * 35)
print(f'Os primeiros 5 colocados são: {brasileirao2018[:5]}', end='\n\n')
print('¨¨' * 35)
print(f'Os últimos 4 colocados são: {brasileirao2018[-4:]}', end='\n\n')
print('¨¨' * 35)
print(
    f'Os times em ordem alfabética são: {sorted(brasileirao2018)}', end='\n\n')
print('¨¨' * 35)
print(
    f'O Chapecoense está na {brasileirao2018.index("Chapecoense") + 1}ª colocação!')
