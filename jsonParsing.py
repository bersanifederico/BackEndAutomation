import json

#
# #create a string having the content of a json file
# courses = '{"name" : "FedericoBersani", "languages" : ["Java", "Python"]}' #json file inside a string
#
# #Load method to parse json string and return a dict
#
# dict_courses = json.loads(courses)
#
# print(type(dict_courses))
#
# print(dict_courses)
#
# print(dict_courses['name'])
#
# #1. extract the list of elements of langauge key
# list_languages = dict_courses['languages']
# print(list_languages)
#
# #2. extract the first element of langauge key
# print(list_languages[0])
#
# #do 1. and 2. in one line
# first_language = dict_courses['languages'][0]
# print(first_language)




#we want to parse content of a json file taken from a folder

with open ('/Users/federicobersani/Desktop/BackEndAutomation/jsonFiles/course.json') as f:
    data = json.load(f)
    print(data)
    print(type(data)) #dict

#access to the second element of the corses
print(data['courses'][1])

#the second element extracted is a dict --> we can extract elements from it
print(data['courses'][1]['title'])

#now we want to extract the website of the dashboard
print(data['dashboard']['website'])




#code that would give me the price of course RPA (considering that the json csn be dinamic and position can change)
#1. understand what we have inside the variable 'courses' and the type of it
print(data['courses'])
print(type(data['courses']))

#2. once understood that we have a list we now know how to iterate over it (using a for)
for course in data['courses']:
    #print(course)
    if course['title'] == 'RPA':
        print(course['price'])
        assert course['price'] == 45 #check the result



#we want to compare 2 dict
#open the second file
with open ('/Users/federicobersani/Desktop/BackEndAutomation/jsonFiles/course1.json') as f2:
    data2 = json.load(f2)

#comparison
assert data == data2 #false/error
