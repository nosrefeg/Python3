import math
catetoOposto = float(input('Digite o valor do cateto oposto: '))
catetoAdjascente = float(input('Digite o valor do cateto oposto: '))
print('Esse é o valor da hipotenusa: {}'.format(
    math.hypot(catetoOposto, catetoAdjascente)))
