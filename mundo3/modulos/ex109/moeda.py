def metade(p=0, format=False):
    p /= 2
    if format:
        return moeda(p)
    else:
        return p


def dobro(p=0, format=False):
    p *= 2
    if format:
        return moeda(p)
    else:
        return p


def aumentar(p=0, percent=0, format=False):
    p += (p * percent) / 100
    if format:
        return moeda(p)
    else:
        return p


def diminuir(p=0, percent=0, format=False):
    p -= (p * percent) / 100
    if format:
        return moeda(p)
    else:
        return p


def moeda(r):
    return f'R${r:.2f}'.replace('.', ',')
