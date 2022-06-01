import mysql.connector
from utilities.configurations import *

#connect to db (old way)
#info needed: host, database, user, psw
# connection = mysql.connector.connect(host = 'localhost', database = 'PythonAutomation',
#                         user = 'root', password = 'Gattomorto96')


#connect to db (NEW WAY)
connection = getConnection()

print(connection.is_connected()) #True
#extract info from db
cursor = connection.cursor()
cursor.execute('select * from CustomerInfo')

#fetch just first line
row = cursor.fetchone()
print(row) #output is a tuple

#retrive third element of a tuple
print(row[2])

#fetch all info of the db
rowAll = cursor.fetchall()
print(rowAll) #output is a list of tuples
#access the 2nd row of the table (second element of the list)
print(rowAll[1])
#IMPORTANT: AFTER YOU DO fetchone(), NEXT TIME YOU FETCH YOU START FROM THE FOLLOWING LINE,
#SINCE ONE LINE WAS ALREADY FETCHED BY THE FIRST COMMAND




