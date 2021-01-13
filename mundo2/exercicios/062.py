termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
parada = 0
i = 1
mais = 10
while mais != 0:
    parada = parada + mais
    while i <= parada:
        print(termo)
        termo += razao
        i += 1
    mais = int(input('''Quer mostrar mais termos? Se sim, digite o valor
            Se não, digite 0!\n '''))
