import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', 
                               password='Pavlovich1985*', 
                               host='127.0.0.1',
                               database='MYDATABASE')

# creating a cursor object using the cursor() method
cursor = conn.cursor()

# preparing SQL query to INSERT a record into the database.
insert_stmt = (
    "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)"
    "VALUES (%s, %s, %s, %s, %s)"
    )
data = ('Ramya', 'Ramapriya', 25, 'F', 5000)

try:
    # executing the SQL command
    cursor.execute(insert_stmt, data)
    # commit changes in the database
    conn.commit()
except:
    # rolling back in case of error
    conn.rollback()

# closing the connection
conn.close()