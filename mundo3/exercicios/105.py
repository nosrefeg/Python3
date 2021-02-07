def notas(* grades, sit=False):
    """
        -> Analisa notas de vários alunos
        :param grades: Pode receber uma ou mais notas
        :param sit: (opcional) Mostrar ou não a situação da turma
        :return: um dicionário com várias informações sobre a situação da turma
    """

    dicNotas = {
        'total': len(grades),
        'maior': max(grades),
        'menor': min(grades),
        'media': sum(grades) / len(grades)
    }
    if sit:
        if dicNotas['media'] >= 7:
            dicNotas['situacao'] = 'BOA'
        elif 5 <= dicNotas['media'] < 7:
            dicNotas['situacao'] = 'RAZOÁVEL'
        else:
            dicNotas['situacao'] = 'RUIM'
    return dicNotas


resultado = notas(6, 4, 8, 3, 2, 7, sit=True)
print(resultado)
help(notas)
