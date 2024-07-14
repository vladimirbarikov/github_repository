import mysql.connector

config = {
    'user': 'root',
    'password': 'Pavlovich1985*',
    'host': '127.0.0.1',
    'database': 'bank',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()