import mysql.connector
from utilities.configurations import *

#connect to db
connection = getConnection()

#check if connection has been established
print(connection.is_connected()) #True
cursor = connection.cursor()

#select info that I want to update
query = 'update customerInfo set Location = %s where CourseName = %s'
data = ('UK','Jmeter')

#update DB with the query
cursor.execute(query,data)

#commint at database lv.
connection.commit()

#close connection
connection.close()