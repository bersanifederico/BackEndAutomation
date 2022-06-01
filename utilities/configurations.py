import configparser
import mysql.connector
from mysql.connector import Error

def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

def getPassword():
    return "Sgabello96"

#connect to DB creating a dict with info required
connect_config = {
    'host' : getConfig()['SQL']['host'],
    'database' : getConfig()['SQL']['database'],
    'user' : getConfig()['SQL']['user'],
    'password' : getConfig()['SQL']['password'],
}

def getConnection():
    try:
        connection = mysql.connector.connect(**connect_config)
        return connection
    except Error as e:
        print(e)


def getQuery(query):

    #connect to DB
    conn = getConnection()
    cursor = conn.cursor()

    #run the query
    cursor.execute(query)

    #from all the result just fetch the first one
    row = cursor.fetchone() #output will be a tuple

    conn.close()
    return row
