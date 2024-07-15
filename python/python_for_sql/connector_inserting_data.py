from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='Pavlovich1985*',
                              host='127.0.0.1',
                              database='employees')
cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ("INSERT INTO employees"
                "(first_name, last_name, hire_date, gender, birth_date)"
                "VALUES (%s, %s, %s, %s, %s)")

add_sallary = ("INSERT INTO salaries"
                "(emp_no, salary, from_date, to_date)"
                "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

data_employee = [('Vladimir', 'Barikov', tomorrow, 'M', date(1985, 8, 30)),
                 ('Aleksandra', 'Barikova', tomorrow, 'F', date(1986, 1, 28)),
                 ('Elena', 'Shved', tomorrow, 'F', date(1965, 5, 18)),
                 ('Pavel', 'Barikov', tomorrow, 'M', date(1965, 3, 23)),
                 ]

cursor.executemany(add_employee, data_employee)
emp_no = cursor.lastrowid

data_salary = {
    'emp_no': emp_no,
    'salary': 50000,
    'from_date': tomorrow,
    'to_date': date(9999, 1, 1),
}


cursor.execute(add_sallary, data_salary)

cnx.commit()

cursor.close()
cnx.close()