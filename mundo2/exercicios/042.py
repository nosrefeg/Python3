lado1 = float(input('Digite o tamanho da reta 1: '))
lado2 = float(input('Digite o tamanho da reta 2: '))
lado3 = float(input('Digite o tamanho da reta 3: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    if lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print('As retas podem formar um triângulo do tipo ESCALENO!')
    elif lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
        print('As retas podem formar um triângulo do tipo EQUILÁTERO!')
    else:
        print('As retas podem formar um triângulo do tipo ISÓSCELES!')


else:
    print('As retas não cumprem a condição de existência de um triângulo!')
