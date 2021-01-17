valores = []

while True:

    numero = int(input('Digite um número: '))
    if numero not in valores:
        valores.append(numero)
        print('Valor adicionado!')
    else:
        print('Valor já existe, não adicionarei!')

    confirmacao = input('Quer continuar? (S/N) ').strip().upper()
    while confirmacao not in 'SN':
        confirmacao = input('Quer continuar? (S/N) ').strip().upper()
    if confirmacao == 'N':
        break

valores.sort()
print('==' * 30)
print(f'Os valores únicos digitados foram {valores}')
