import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', 
                               password='Pavlovich1985*', 
                               host='127.0.0.1')

# creating a cursor object using the cursor() method
cursor = conn.cursor()

# doping database MYDATABASE if already exists
cursor.execute("DROP database IF EXISTS MYDATABASE")

# retrieving the list of databases
print("List of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

# closing the connection
conn.close()