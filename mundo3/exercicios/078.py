valores = []
for i in range(0, 5):
    valores.append(int(input('Digite um número: ')))
print(f'''Você digitou os valores {valores}
O maior valor foi {max(valores)} na posição {valores.index(max(valores))} e o menor valor foi {min(valores)} na posição {valores.index(min(valores))}''')
