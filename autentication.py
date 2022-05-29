#Autentication
import requests
from utilities.configurations import *

# url = 'https://api.github.com/user'
# githubResponse = requests.get(url, verify = False, auth=('bersanifederico',getPassword()))
# print(githubResponse.status_code)


url2 = 'https://api.github.com/user/repos'
# response = requests.get(url2, verify = False, auth = ('bersanifederico',getPassword()))
# print(response.status_code)


#next level
se = requests.session()
se.auth = auth = ('bersanifederico',getPassword())

response = se.get(url2)
print(response.status_code)