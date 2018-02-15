import pymongo
import json

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection.askreddit
ar = db.posts

filename = "AskReddit.json"
file = open(filename, "r")
contents = file.read()

jsoncont = json.loads(contents)
posts2 = jsoncont["data"]["children"]

ar.insert_many(posts2)
'''
for x in posts2:
    print x
'''
