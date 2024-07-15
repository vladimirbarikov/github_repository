from sqlalchemy import create_engine
import pymysql
import pandas as pd

sql_engine = create_engine('mysql+pymysql://root:Pavlovich1985*@127.0.0.1/newdb')

db_connection = sql_engine.connect()

df = pd.read_sql("select * from newdb.vitals", db_connection);

pd.set_option('display.expand_frame_repr', False)

print(df)

db_connection.close()