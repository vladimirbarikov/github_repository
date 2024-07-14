import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', 
                               password='Pavlovich1985*', 
                               host='127.0.0.1', 
                               database='bank')

# creating a cursor object using the cursor() method
cursor = conn.cursor()

# executing MYSQL function using execute() method
cursor.execute('select database()')

# fetch a single row using fetchone() method
data = cursor.fetchone()

print('connection established to:' , data)

# closing the connection
conn.close()