import phonenumbers
from phonenumbers import geocoder, carrier

# Ajustando o número para usar no phonenumbers
telefone = '+5511999909721'

telefone_corrigido = phonenumbers.parse(telefone)
print(telefone_corrigido)

#  Localizando a origem do número
local = geocoder.description_for_number(telefone_corrigido, 'pt-br')
print(local)

# Formatando o número
telefone_formatado = phonenumbers.format_number(telefone_corrigido,
                                                phonenumbers.PhoneNumberFormat.NATIONAL)
print(telefone_formatado)

# Descobrindo a operadora
operadora = carrier.name_for_number(telefone_corrigido, 'pt-br')
print(operadora)

# Pegando um número de telefone de um texto
texto = '''
Testando um teste para ser testado

Olá, PE
87999999999
valeu
11988787822'''
for tel in phonenumbers.PhoneNumberMatcher(texto, 'BR'):
    print(tel)