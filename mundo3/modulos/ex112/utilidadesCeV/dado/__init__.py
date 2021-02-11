def leiaDinheiro(msg):
    while True:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[32mERRO: "{valor}" não é um preço válido!\033[m')
        else:
            valor = float(valor)
            break
    return valor
