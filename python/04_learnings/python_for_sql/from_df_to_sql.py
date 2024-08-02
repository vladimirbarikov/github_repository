from sqlalchemy import create_engine
import pymysql
import pandas as pd

vitals = {"id":["01", "02", "03", "04", "05", "06", "07"],
          "favourite":["Salad", "Steak", "Burger", "Chicken", "Salmon", "Pot", "Banana"],
          "frequency":[5, 1, 2, 2, 7, 6, 1],
          "highest":[30, 20, 16, 23, 20, 26, 9],
          "last":[21,20,4,11,7,7,7],
          "rating":[3,3,3,2,3,2,4],
          "avg_rating":[3,4,2,1,3,4,3],
          "mode":["Web", "App", "App", "App", "Web", "Web", "App"],
          "care":["No", "No", "No", "No", "Yes", "No", "No"]};

table_name = "vitals"

df = pd.DataFrame(data=vitals)

sql_engine = create_engine('mysql+pymysql://root:Pavlovich1985*@127.0.0.1/newdb')

db_connection = sql_engine.connect()

try:
    frame = df.to_sql(table_name, db_connection, if_exists='fail');
except ValueError as vx:
    print(vx)
except Exception as ex:
    print(ex)
else:
    print("Table %s created successfully."%table_name);
finally:
    db_connection.close()