frase = input('Digite uma frase: ').strip().lower()
print('''Há {} as na frase
Aparece primeiro na posição {}
E a ultima na posição {}'''.format(frase.count('a'), frase.find('a') + 1, frase.rfind('a')+1))
