from utilities.configurations import *

def addBookpayload():
    body = {

    "name":"Learn Appium Automation with Java",
    "isbn": "bcdron",
    "aisle":"22797",
    "author":"John foe"
    }
    return body

suck

def buildPayloadFromDB(query):
    addBody = {}

    #read query and extract as tuple
    tp = getQuery(query)

    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]

    return addBody