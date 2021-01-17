expressao = input('Digite uma expressão matematica com parênteses: ').strip()
lista = []
for af in expressao:
    if af == '(':
        lista.append('(')
    elif af == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

print('ºº' * 25)
if len(lista) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão NÃO é valida!')
