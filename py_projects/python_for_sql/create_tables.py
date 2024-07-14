import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', 
                               password='Pavlovich1985*', 
                               host='127.0.0.1',
                               database='MYDATABASE')

# creating a cursor object using the cursor() method
cursor = conn.cursor()

# creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
FIRST_NAME CHAR(20) NOT NULL,
LAST_NAME CHAR(20),
AGE INT,
SEX CHAR(1),
INCOME FLOAT)'''
cursor.execute(sql)

# closing the connection
conn.close()