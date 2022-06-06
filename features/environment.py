import requests
import json


def after_scenario(context, scenario):
    response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={
        'ID': context.ID
    }, headers={'Content-Type': 'application/json'}, )

    assert response_deleteBook.status_code == 200

    response_deleteBook_json = response_deleteBook.json()
    print(response_deleteBook_json)

    assert response_deleteBook_json["msg"] == "book is successfully deleted"


