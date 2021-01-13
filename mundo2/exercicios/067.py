num = i = mult = 1
while True:
    print('-¨' * 35)
    num = int(
        input("Digite um número para ver sua tabuada(número negativo para parar): "))
    print('-¨' * 35)
    i = 1
    if num < 0:
        break
    while i < 10:
        mult = num * i
        print(f'{num} x {i} = {mult}')
        i += 1
