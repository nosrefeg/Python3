from datetime import date


def voto(nasc):
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!'
    elif 18 > idade >= 16 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


print('--' * 30)
dataNasc = int(input('Em que ano você nasceu? '))
print(voto(dataNasc))
