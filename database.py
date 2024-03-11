import json

import psycopg2

connection = psycopg2.connect(
    database="trader-db",
    user="postgres",
    password="1",
    host="localhost",
    port=5432
)

if(connection):
    print("ok")


# cursor = connection.cursor()
#
# cursor.execute("SELECT * from portal.portal_users;")
#
# # Fetch all rows from database
# record = cursor.fetchall()
#
# print("Data from Database:- ", record)