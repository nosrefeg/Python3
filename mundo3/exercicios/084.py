pessoas = []
maior = menor = 0

while True:
    info = [input('Digite seu nome: '), float(input('Digite seu peso: '))]
    confirm = input('Quer continuar? (S/N) ').strip().upper()

    if len(pessoas) == 0:
        maior = menor = info[1]
    else:
        if info[1] > maior:
            maior = info[1]
        else:
            menor = info[1]
    pessoas.append(info[:])

    while confirm not in 'SN':
        confirm = input('Quer continuar? (S/N) ').strip().upper()
    if confirm == 'N':
        break

print('¨¨' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A pessoa com maior peso, de {maior} quilos, foi ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nA pessoa com maior peso, de {menor} quilos, foi ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
