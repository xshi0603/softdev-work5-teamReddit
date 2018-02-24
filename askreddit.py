'''
dataset: AskReddit
description: A list of posts on the subreddit /r/AskReddit. It includes information of each post such as its author, its url, its upvotes/downvotes, and much much more.
download: https://www.reddit.com/r/AskReddit.json
summary of import: We first read the .json file using open() and .read(). Then we turn the contents into a python dictionary using json.loads(). After this, we used created a list of the posts using jsoncont["data"]["children"] (there was additional information about the subreddit). The we used insert_many() to import it into the database.
'''

import pymongo
import json

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection.askreddit
ar = db.posts

filename = "AskReddit.json"
file = open(filename, "r")
contents = file.read()

jsoncont = json.loads(contents)
print jsoncont
posts2 = jsoncont["data"]["children"]

ar.insert_many(posts2)

file.close()

x = ar.find({"data.link_flair_css_class": "serious"})
for post in x:
    print post

y = ar.find({"data.author": "J-Bradley1"})
for post in y:
    print post

c = ar.find( { "data.score": { "$gt": 50 } } )
for post in c:
    print post
