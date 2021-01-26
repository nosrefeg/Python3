from datetime import date
worker = {
    'nome': input('Nome: '),
    'idade': date.today().year - int(input('Ano de nascimento: ')),
    'ctps': int(input('Carteira de Trabalho (0 caso não tenha): '))
}
if worker['ctps'] > 0:
    worker['contratacao'] = int(input('Ano de contratação: '))
    worker['salario'] = float(input('Salário: R$ '))
    if date.today().year - worker['contratacao'] > 35:
        worker['aposentadoria'] = 'Já pode se aposentar'
    else:
        worker['aposentadoria'] = 35 - (date.today().year -
                                        worker['contratacao']) + worker['idade']
    for k, v in worker.items():
        print(f'{k} tem o valor de {v}')
else:
    for k, v in worker.items():
        print(f'{k} tem o valor de {v}')
