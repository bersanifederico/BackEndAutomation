#Autentication
import requests
from utilities.configurations import *

url = 'https://api.github.com/user'
githubResponse = requests.get(url, verify = False, auth=('bersanifederico',getPassword()))
print(githubResponse.status_code)
