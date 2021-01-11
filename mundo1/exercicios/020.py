import random

aluno1 = input('Digite o nome dos aluno 1: ')
aluno2 = input('Digite o nome dos aluno 2: ')
aluno3 = input('Digite o nome dos aluno 3: ')
aluno4 = input('Digite o nome dos aluno 4: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
print('A ordem de apresentação é:')
random.shuffle(alunos)
print(alunos)
