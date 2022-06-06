from utilities.configurations import *

def addBookpayload(isbn, aisle):
    body = {

    "name":"Learn Appium Automation with Java",
    "isbn": isbn,
    "aisle":aisle,
    "author":"John foe"
    }
    return body



def buildPayloadFromDB(query):
    addBody = {}

    #read query and extract as tuple
    tp = getQuery(query)

    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]

    return addBody