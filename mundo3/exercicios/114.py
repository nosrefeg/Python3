import requests

try:
    rq = requests.get('http://pudim.com.br')
except:
    print('\033[1;32mO site "pudim.com.br" não está acessível no momento!\033[m')
else:
    print('\033[1;33mO site "pudim.com.br" está acessível no momento!\033[m')
