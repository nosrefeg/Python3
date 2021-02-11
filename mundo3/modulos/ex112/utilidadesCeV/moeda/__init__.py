def metade(p, format=False):
    p /= 2
    if format:
        return moeda(p)
    else:
        return p


def dobro(p, format=False):
    p *= 2
    if format:
        return moeda(p)
    else:
        return p


def aumentar(p, percent, format=False):
    p += (p * percent) / 100
    if format:
        return moeda(p)
    else:
        return p


def diminuir(p, percent, format=False):
    p -= (p * percent) / 100
    if format:
        return moeda(p)
    else:
        return p


def moeda(r):
    return f'R${r:.2f}'.replace('.', ',')


def resumo(p, aumenta, reduz):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'{"Preço analisado:":<20}', end=' ')
    print(f'{moeda(p):>18}')
    print(f'{"Dobro do preço:":<20}', end=' ')
    print(f'{dobro(p, True):>18}')
    print(f'{"Metade do preço:":<20}', end=' ')
    print(f'{metade(p, True):>18}')
    print(f'{aumenta}{"% de aumento:":<20}', end=' ')
    print(f'{aumentar(p, aumenta, True):>16}')
    print(f'{reduz}{"% de redução:":<20}', end=' ')
    print(f'{diminuir(p, reduz, True):>16}')
    print('-' * 40)
