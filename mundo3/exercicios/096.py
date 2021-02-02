def area(largura, comprimento):
    print('--' * 30)
    print(f'''O terreno tem {largura} metros de largura e {comprimento} de comprimento!
        Uma aréa total de {largura * comprimento} metros! ''')
    print('--' * 30)


print('--' * 30)
print(f'{"ARÉA DO TERRENO":^60}')
print('--' * 30)
largura = float(input('Largura do terreno, em metros: '))
comprimento = float(input('Comprimento do terreno, em metros: '))
area(largura, comprimento)
