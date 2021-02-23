def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'a')
        a.close()
    except:
        print('ERRO na criação do arquivo!')
    else:
        print(f'{nome} criado com sucesso!')


def verPessoas(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo!')
    else:
        print('-' * 50)
        print(f'{"PESSOAS CADASTRADAS":^50}')
        print('-' * 50)
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30} {dados[1]:>10} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='Desconhecido', idade=0):
    print('-' * 50)
    print(f'{"NOVO CADASTRO":^50}')
    print('-' * 50)
    try:
        a = open(arquivo, 'at')
    except:
        print('ERRO ao ler arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO ao escrever no arquivo!')
        else:
            print(f'Novo registro de {nome} foi adicionado!')
            a.close()
