#!/usr/bin/python3.7.1

#importing packages
from subprocess import run
import requests
import json
import urllib.request
import random

#unsplash url for random photos & the client_id from mt developer account
url = "https://api.unsplash.com/photos/random"
my_client_id = "" #will keep private for now

#prompts user for terms that will be used to search and stores in a list
#   will be adding additional functionality here
queries = []
for i in range(3):
    term = input("Provide a search term: ")
    queries.append(term)

#selects a random term to search Unsplash for from given terms
term = random.choice(queries)

#search parameters for on-topic photos and correct orientation for desktop backgrounds
search = {"query": term, "orientation": "landscape"}

#Header argument is provided by Unsplash to ensure v1 photos are the only results returned
response = requests.get(url + my_client_id,
                        headers={"Accept-Version": 'v1'}, params = search)

#loading the returned data into a readable format
x = json.loads(response.content)

#using pprint package for human readability, will remove after file is completed.
# # pprint(x)

#store all image links into variable, then pulling the "raw" image url from that variable
links = x['urls']
download = links['raw']
print(download)

#create filename with unique string of characters from the url and inserting into the Applescript that will update the desktop background
filename = download[34:41] + ".jpg"
script = "osascript -e 'tell application \"System Events\" to tell every desktop to set picture to \"~/Desktop/unsplash_program/" + filename + "\"'"
#print(filename)

#downloaded the image using raw url and saving under unique file name (non-unique produces a bug)
urllib.request.urlretrieve(download, download[34:41] + ".jpg")
#"background" + download[34:41] + ".jpg")

#this shell script will set background as the downloaded image without feedback
#   osascript -e 'tell application "System Events" to tell every desktop to set picture to "~/          Desktop/unsplash_program/background.jpg"'

run(script, shell=True)

file = open("photo_urls.txt","a+")
file.write(str(datetime.datetime.today().strftime('%Y-%m-%d')) + ": " + download + "\n")

os.remove(filename)
