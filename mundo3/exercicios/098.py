from time import sleep
print('-' * 30)
print('Contagem de 1 a 10, de 1 em 1:')
for i in range(1, 11):
    print(i, end=' ', flush=True)
    sleep(0.5)
print()
print('-' * 30)
print('Contagem de 10 a 0, de 2 em 2:')
for i in range(10, -1, -2):
    print(i, end=' ', flush=True)
    sleep(0.5)
print()


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} a {fim}, de {passo} em {passo}:')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= passo
    print()
    print('--' * 30)


print('--' * 30)
print('     CONTADOR PERSONALIZADO     ')
inicio = int(input('Digite o valor inicial da contagem: '))
fim = int(input('Digite o valor final da contagem: '))
passo = int(input('Digite o valor do passo da contagem: '))
print('--' * 30)
contador(inicio, fim, passo)
