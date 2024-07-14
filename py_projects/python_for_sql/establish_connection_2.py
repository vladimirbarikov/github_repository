from mysql.connector import (connection)

# establishing the connection
conn = connection.MySQLConnection(user='root', 
                                  password='Pavlovich1985*', 
                                  host='127.0.0.1', 
                                  database='bank')

# closing the connection
conn.close()