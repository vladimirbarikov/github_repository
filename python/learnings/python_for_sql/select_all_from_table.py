import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', 
                               password='Pavlovich1985*', 
                               host='127.0.0.1',
                               database='MYDATABASE')

# creating a cursor object using the cursor() method
cursor = conn.cursor()

# preparing query to show all data from table EMPLOYEE
sql = "SELECT * FROM EMPLOYEE";

# retrieving the data of table EMPLOYEE
print("All inserted data in table EMPLOYEE: ")
cursor.execute(sql)
print(cursor.fetchall())

# closing the connection
conn.close()