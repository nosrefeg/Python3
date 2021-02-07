def fatorial(numero, show=False):
    """
        -> Calcula o Fatorial de um número
        :param numero: O valor do fatorial a ser calculado
        :param show: (opcional) Mostrar ou não o calculo
        :return: O valor fatorial da variavel numero 
    """
    f = 1
    for i in range(numero, 0, -1):
        if show:
            if i == 1:
                print(f'{i} = ', end='')
            else:
                print(f'{i} x ', end='')
        f *= i
    return f


print('--' * 30)
print(fatorial(7, True))
help(fatorial)
