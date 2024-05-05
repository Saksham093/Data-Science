import mysql.connector
import pandas as pd

data = pd.read_csv(r'used_bikes.csv')

# sql connect...
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Saksham#MySQL",
    database="neenopal"
)

cursor = mydb.cursor()

# Create Database neenopal...
# cursor.execute("CREATE DATABASE neenopal")

# Create Table used_bikes...
# cursor.execute("create table used_bikes(brand varchar(20),"
#                "bike_name varchar(50),"
#                "price float8,"
#                "city varchar(20),"
#                "kms_driven float8,"
#                "owner varchar(20),"
#                "age int,"
#                "power int)")


table_name = 'used_bikes'
column_name = 'bike_name'


cursor.execute(f"SHOW INDEX FROM {table_name} WHERE Key_name='idx_{column_name}'")
index_exists = cursor.fetchall()

# drop index
if index_exists:
    cursor.execute(f"DROP INDEX idx_{column_name} ON {table_name}")

# inserting data
data_tuples = [tuple(row) for row in data.values]


sql_insert = f"INSERT INTO {table_name}(brand, bike_name, price, city, kms_driven, owner, age, power) VALUES (%s, " \
             f"%s, %s, %s, %s, %s, %s, %s) "


cursor.executemany(sql_insert, data_tuples)

# inserting index
cursor.execute(f"CREATE INDEX idx_{column_name} ON {table_name}({column_name})")


# Fetch the data from the table
query = f"SELECT * FROM {table_name}"
result_df = pd.read_sql_query(query)

# Display the result
print(result_df)


cursor.close()
mydb.close()
