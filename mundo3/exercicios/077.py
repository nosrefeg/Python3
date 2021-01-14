words = ('palavra', 'teto', 'teste', 'arroz', 'evento', 'maneira')
for w in words:
    print(f'Na palavra {w.upper()} existem as vogais: ', end='')
    for l in w:
        if l.upper() in 'AEIOU':
            print(l, end=' ')
    print('')
