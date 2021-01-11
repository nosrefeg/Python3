distancia = int(input('Digite a distância da viagem: '))
if distancia <= 200:
    print('O preço da viagem é: R${:.2f}'.format(distancia * 0.50))
else:
    print('O preço da viagem é: R${:.2f}'.format(distancia * 0.45))
