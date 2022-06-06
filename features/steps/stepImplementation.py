from behave import *
from payload import *
from utilities.configurations import *
from utilities.resources import *

import requests



@given ('the Book details which needs to be added to Library')
def stepImplementation(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json'}
    context.payload = addBookpayload("albsl","433") #not necessary just to make it nicer


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.add_book = requests.post(context.url, json=context.payload, headers=context.headers, )


@then('book is successfully added')
def step_impl(context):
    add_book_responses = context.add_book.json()
    print(add_book_responses)

    # extract ID
    context.ID = add_book_responses['ID']
    print(context.ID)
    assert add_book_responses["Msg"] == "successfully added"


@given ('the Book details with {isbn} and {aisle}')
def step_impl(context,isbn,aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json'}
    context.payload = addBookpayload(isbn, aisle)  # not necessary just to make it nicer