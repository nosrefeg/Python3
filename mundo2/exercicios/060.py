num = int(input('Digite um número: '))
fat = 1
i = num
while i > 0:
    fat *= i
    i -= 1

print('O fatorial de {} é {}'.format(num, fat))
