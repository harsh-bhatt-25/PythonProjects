#pip install mysql-connector-python
#Need to install this to connect with the database
#This file is used to add data from csv files to a database

import mysql.connector as MySQL
import mysql.connector as errorcode
import os
from csv import reader, writer
import random
import time

conn = MySQL.connect(
    host="localhost",
    database="business",
    user="root",
    password="password"
)
cur = conn.cursor()

DB_NAME = "business"
# TABLES = {}
#
# TABLES["Cities"] = (
#     "CREATE TABLE `Cities`("
#     "`PostOfficeName` varchar(45),"
#     "`Pincode` int(10),"
#     "`District Name` varchar(45),"
#     "`City` varchar(45),"
#     "`State` varchar(45)"
#     ") ENGINE=InnoDB")
#
# for table_name in TABLES:
#     table_description = TABLES[table_name]
#     try:
#         print("Creating Table {}: ".format(table_name), end='')
#         cur.execute(table_description)
#     except MySQL.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("Already Exists")
#         else:
#             print(err.msg)
#     else:
#         print("OK")

cityfile = open(r"C:\Users") # a csv file
csvReader = reader(cityfile)
next(csvReader)

for row in csvReader:
    # try:
    print(row)
    cur.execute("INSERT INTO color VALUES (%s, %s)",
                (row[0], row[1]))
    conn.commit()
    # except:
    #     break

cur.close()
conn.commit()
conn.close()
