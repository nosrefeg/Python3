def metade(p):
    p /= 2
    return p


def dobro(p):
    p *= 2
    return p


def aumentar(p, percent):
    p += (p * percent) / 100
    return p


def diminuir(p, percent):
    p -= (p * percent) / 100
    return p


def moeda(r):

    return f'R${r:.2f}'.replace('.', ',')
