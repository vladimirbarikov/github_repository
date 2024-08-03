import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', 
                               password='Pavlovich1985*', 
                               host='127.0.0.1',
                               database='bank')

# creating a cursor object using the cursor() method
cursor = conn.cursor()

# retrieving single row
sql = '''SELECT * FROM employee'''

# executing the query
cursor.execute(sql)

# fetching the 1st row from the table
result1 = cursor.fetchone();
print(result1)

# fetching next 4 rows from the table
result2 = cursor.fetchmany(size=4);
print(result2)

# closing the connection
conn.close()