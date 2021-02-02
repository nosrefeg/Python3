def escreva(texto):
    print('-' * (len(texto) + 2))
    print(texto)
    print('-' * (len(texto) + 2))


texto = input('Digite uma frase: ').strip()
escreva(texto)
