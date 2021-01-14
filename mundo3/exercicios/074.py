from random import randint
menor = maior = 0
aleatorios = (randint(0, 20), randint(0, 20), randint(
    0, 20), randint(0, 20), randint(0, 20))

print(f'''Os valores sorteados foram {aleatorios}
O maior valor entre eles é {max(aleatorios)}
O menor valor entre eles é {min(aleatorios)}''')
# for i in range(0, 5):
#     if i == 0:
#         menor = maior = aleatorios[0]
#     else:
#         if maior > aleatorios[i]:
#             menor = aleatorios[i]
#         elif menor < aleatorios[i]:
#             maior = aleatorios[i]
# print(f'''Os valores sorteados foram {aleatorios}
# O maior valor entre eles é {maior}
# O menor valor entre eles é {menor}''')
