from random import randint
numeros = []


def sorteia():
    for i in range(0, 5):
        numeros.append(randint(0, 10))


def soma(lista):
    somaPar = 0
    for i in lista:
        if i % 2 == 0:
            somaPar += i
    print(f'A soma dos valores pares de {lista} é {somaPar}')


sorteia()
soma(numeros)
