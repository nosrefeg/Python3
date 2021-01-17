valores = []

for i in range(0, 5):
    numero = int(input('Digite um número: '))

    if i == 0 or numero > valores[-1]:
        valores.append(numero)
        print('Valor adicionado no final da lista!')
    else:
        c = 0
        while c < len(valores):
            if numero <= valores[c]:
                valores.insert(c, numero)
                print('Valor adicionado na posição {c} da lista!')
                break
            c += 1

print('##' * 30)
print(f'Os valores digitados em ordem crescente são: {valores}')
