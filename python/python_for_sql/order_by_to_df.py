from sqlalchemy import create_engine
import pymysql
import pandas as pd

sql_engine = create_engine('mysql+pymysql://root:Pavlovich1985*@127.0.0.1/MYDATABASE')

db_connection = sql_engine.connect()

df_age = pd.read_sql("select * from MYDATABASE.EMPLOYEE order by AGE", db_connection);
df_income = pd.read_sql("select * from MYDATABASE.EMPLOYEE order by INCOME desc", db_connection);

pd.set_option('display.expand_frame_repr', False)

print(df_age)
print(df_income)

db_connection.close()