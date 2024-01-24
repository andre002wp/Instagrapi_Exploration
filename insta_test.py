import json
import os
from instagrapi import Client

with open('credentials.json') as json_file:
    data = json.load(json_file)
    username,password = data['username'],data['password']

cl = Client()
  
if not cl.load_settings("session.json"):
    IG_USERNAME = os.getenv("IG_USERNAME", "default_username")
    IG_PASSWORD = os.getenv("IG_PASSWORD", "")
    cl.login(IG_USERNAME, IG_PASSWORD) 
    cl.dump_settings("session.json")

hashtag = "presidenbaru"

media = cl.hashtag_medias_recent(hashtag, amount=5)

for i, md in enumerate(media):
    print(md)
    print(md.__getattribute__)
    print("new\n\n\n")