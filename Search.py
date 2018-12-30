import requests
import json
from pprint import pprint

url = "https://api.unsplash.com/search/photos/"
my_client_id = "?client_id=c220750f96347e0439d77a2bdbba9d916f1a1a4604196e35804d2c6a4ac4c731"
orientation = "landscape"
search = {"query": "ocean", "per_page": 1}


response = requests.get(url + my_client_id, 
    headers={"Accept-Version": 'v1'}, params = search)

x = json.loads(response.content)

pprint(x)