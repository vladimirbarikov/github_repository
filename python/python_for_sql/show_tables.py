import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', 
                               password='Pavlovich1985*', 
                               host='127.0.0.1',
                               database='MYDATABASE')

# creating a cursor object using the cursor() method
cursor = conn.cursor()

# retrieving the list of tables
print("List of databases: ")
cursor.execute("SHOW TABLES")
print(cursor.fetchall())

# closing the connection
conn.close()