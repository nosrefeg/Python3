aluno = {
    'nome': input('Digite o nome do aluno: '),
    'media': float(input('Digite a média: '))
}
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'RECUPERAÇÃO'
else:
    aluno['situacao'] = 'REPROVADO'

print('--' * 10)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
