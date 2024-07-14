import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', 
                               password='Pavlovich1985*', 
                               host='127.0.0.1',
                               database='MYDATABASE')

# creating a cursor object using the cursor() method
cursor = conn.cursor()

# retrieving specific records using the ORDER BY clause
cursor.execute("SELECT * from EMPLOYEE ORDER BY INCOME DESC")

print(cursor.fetchall())

# closing the connection
conn.close()