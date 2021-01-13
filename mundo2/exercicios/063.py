n = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
i = 3
print('{} | {} | '.format(t1, t2), end='')
while i <= n:
    t3 = t1 + t2
    print('{} | '.format(t3), end='')
    t1 = t2
    t2 = t3
    i += 1
print('DEU BOM')
