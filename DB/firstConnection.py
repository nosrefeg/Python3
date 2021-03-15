import mysql.connector

banco = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Geferson00",
    database="padaria"
)

cursor = banco.cursor()

cursor.execute(
    'create table paes(id int not null auto_increment key, nome varchar(20) not null, preco float not null)')
