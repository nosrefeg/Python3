nome = preco = total = mmil = nomeb = menor = i = stop = 0
while True:
    nome = input('Digite o nome do produto: ').strip()
    preco = float(input('Digite o preco do produto: '))
    total += preco
    if preco > 1000:
        mmil += 1
    if i == 0:
        menor = preco
    else:
        if menor > preco:
            menor = preco
            nomeb = nome
    stop = input('Quer continuar? (S/N) ').strip().upper()
    while stop not in 'SN':
        stop = input('Quer continuar? (S/N) ').strip().upper()
    if stop == 'N':
        break
    i += 1
print(
    f'O total gasto foi de R${total:.2f}, com {mmil} produtos custando mais de R$1000 e o produto mais barato é {nomeb}!')
