#import packages
import requests
import json
# from pprint import pprint
import random

url = "https://api.unsplash.com/photos/random"
my_client_id = "?client_id=" #client_id is to be kept secret

#prompts user for terms that will be used to search
queries = []
for i in range(3):
    term = raw_input("Provide a search term: ")
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

