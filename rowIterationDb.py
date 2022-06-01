import mysql.connector
from utilities.configurations import *

#connect to db
connection = getConnection()

#check if connection has been established
print(connection.is_connected()) #True

#extract info from db
cursor = connection.cursor()
cursor.execute('select * from CustomerInfo')

#fetch all rows
rows = cursor.fetchall()
print(type(rows))

#iterate over rows to get the amount (3rd position)
sum_amount = 0
for row in rows:
    sum_amount += row[2]

print(sum_amount)

#good practice to close the connection once the process is done
connection.close()