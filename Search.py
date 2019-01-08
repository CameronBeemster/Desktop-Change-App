#!/usr/bin/python3.7.1

from subprocess import run
import requests
import json
import urllib.request
import random

url = "https://api.unsplash.com/photos/random"
my_client_id = "" #will keep private for now

#prompts user for terms that will be used to search
queries = []
for i in range(3):
    term = input("Provide a search term: ")
    queries.append(term)

#selects a random term to search Unsplash for
term = random.choice(queries)

search = {"query": term, "orientation": "landscape"}

#Header argument is provided by Unsplash to ensure v1 photos are the only results returned
response = requests.get(url + my_client_id,
                        headers={"Accept-Version": 'v1'}, params = search)

x = json.loads(response.content)

#using pprint package for human readability, will remove after file is completed.
# # pprint(x)

links = x['urls']
download = links['raw']
print(download)

filename = download[34:41] + ".jpg"
script = "osascript -e 'tell application \"System Events\" to tell every desktop to set picture to \"~/Desktop/unsplash_program/" + filename + "\"'"
#print(filename)

#working retrieval
urllib.request.urlretrieve(download, download[34:41] + ".jpg")
#"background" + download[34:41] + ".jpg")


# this shell script will set background as the downloaded image without feedback
# osascript -e 'tell application "System Events" to tell every desktop to set picture to "~/Desktop/unsplash_program/background.jpg"'

#run("./resetBackground.sh")
#run("./setBackground.sh")
run(script, shell=True)
