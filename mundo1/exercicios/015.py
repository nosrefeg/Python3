dias = float(input('Digite por quantos dias o carro foi alugado: '))
km = float(input('Digite quantos KM o carro rodou: '))
total = (dias * 60) + (km * 0.15)
print('O valor total pelo carro alugado é {} reais'.format(total))
