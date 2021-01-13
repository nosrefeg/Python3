# As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

string = '22'
print(string)
print(type(string))

tupla = (1, 2, 3, 3, 4, 5)
print(tupla[0:4])
print(type(tupla))

for i in tupla:
    print(i)
