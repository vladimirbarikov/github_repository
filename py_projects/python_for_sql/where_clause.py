import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', 
                               password='Pavlovich1985*', 
                               host='127.0.0.1',
                               database='MYDATABASE')

# creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = '''CREATE TABLE EMPLOYEE(FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20), AGE INT, SEX CHAR(1), INCOME FLOAT)'''

cursor.execute(sql)

# populating the table
insert_stmt = "INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (%s, %s, %s, %s, %s)"

data = [('Krishna', 'Sharma', 19, 'M', 2000), 
        ('Raj', 'Kandukuri', 20, 'M', 7000), 
        ('Ramya', 'Ramapriya', 25, 'F', 5000), 
        ('Mac', 'Mohan', 26, 'M', 2000)]

cursor.executemany(insert_stmt, data)

conn.commit()

# retrieving specific records using the where clause
cursor.execute("SELECT * from EMPLOYEE WHERE AGE < 23")
print(cursor.fetchall())

# closing the connection
conn.close()