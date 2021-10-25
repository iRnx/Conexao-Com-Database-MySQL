import mysql.connector

cursor = ''
# Conectar ao seu banco de dados #
con = mysql.connector.connect(host='localhost', database='python', user='root', password='root')

if con.is_connected():   # para saber se vc esta conectado #
    db_info = con.get_server_info()   # para pegar a versão do servidor #
    print(f'Conectado ao servidor MySQL versão: {db_info}')
    cursor = con.cursor()
    cursor.execute('SELECT database()')  # para executar comandos SQL #
    linha = cursor.fetchone()  # Para retornar apenas uma linha do resultado que obteve no select #
    print(f'Conectado ao banco de dados: {linha}')

# Para finalizar a conexão #
if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão ao MySQL foi encerrada')
