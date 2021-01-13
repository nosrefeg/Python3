termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
i = 1
# for i in range(termo, termo + 10 * razao, razao):
#     print(i)

while i <= 10:
    print(termo)
    termo += razao
    i += 1
