t = '  e ae moral,relou mai frend, rau are u  '

print('MÉTODOS DE ANÁLISE')

print(len(t))
print(t.count('e'))
print(t.count('e', 0, 21))  # count com fatiamento
print(t.find('au'))
print('mai' in t)
print('------------------------------------------')

print('MÉTODOS DE FATIAMENTO')
print(t[2])
print(t[2:7])
print(t[2:8:2])
print(t[:6])
print(t[5:])
print(t[4::3])
print('------------------------------------------')

print('MÉTODOS DE TRANSFORMAÇÃO')

print(t.replace('e', 'a'))
print(t.upper())
print(t.lower())
print(t.capitalize())
print(t.title())
print(t.strip())  # remove os espaços inuteis no inicio e final
print(t.rstrip())  # remove só os ultimos espaços
print(t.lstrip())  # remove só os primeiros espaços
print('------------------------------------------')

print('MÉTODOS DE DIVISÃO')

t1 = 'olá amigo, como estás?'

print(t1.split())
t2 = t1.split()
# split() retorna um array com os elementos delimitados pelo parametro passado

print('-_-'.join(t2))
# join() junta os elementos de um array, formando uma string
