from datetime import date
demaior = 0
demenor = 0
for i in range(0, 7):
    nasc = int(input('Digite sua data de nascimento: '))
    if date.today().year - nasc < 18:
        demenor += 1
    else:
        demaior += 1
print('{} pessoas são maiores de idade e {} pessoas ainda não são maiores de idade'.format(
    demaior, demenor))
