import mysql.connector

# Conectando ao MySQL e ao banco de dados
banco = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Geferson00",
    database="padaria"
)

cursor = banco.cursor()

# Criando uma tabela
# cursor.execute('create table paes(id int not null auto_increment key, nome varchar(20) not null, preco float not null)')

# Inserindo na tabela
# comandoSQL = 'INSERT INTO paes (nome, preco) VALUES (%s, %s)'
# data = ('De açucar', '0.35')
# cursor.execute(comandoSQL, data)
# banco.commit()

# Recuperando os dados da tabela
# cursor.execute('SELECT * FROM paes WHERE preco>2.5')
# informacaoDaTabela = cursor.fetchall()
# print(informacaoDaTabela)

# Deletando dados da tabela
cursor.execute('DELETE FROM paes WHERE nome = "De açucar" ')
banco.commit()
