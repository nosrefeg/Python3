from biblioteca.interface import *
from biblioteca.arquivo import *
from time import sleep

arq = 'pessoasCadastradas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    opcao = menu()
    if opcao == 1:
        verPessoas(arq)
    elif opcao == 2:
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        sair()
        break
    else:
        print('\033[0;32mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)
