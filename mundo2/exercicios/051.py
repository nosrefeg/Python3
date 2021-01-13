termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
for i in range(termo, termo + 10 * razao, razao):
    print(i)
