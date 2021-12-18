from logging import error, exception
from os import environ
import requests
from apis import ACCESS_KEY, ACCESS_SECRET, auth, api
from os.path import join, dirname
try:
    from dotenv import load_dotenv
except ImportError:
    print("No module named 'google' found")
from os import environ as env

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

querystring = {"print":"pretty"}
id_list = "https://hacker-news.firebaseio.com/v0/newstories.json"
response_of_list = requests.request("GET", id_list).json()

id_of_post = response_of_list[0]
print(id_of_post)
url = f"https://hacker-news.firebaseio.com/v0/item/{id_of_post}.json?print=pretty"

response = requests.request("GET", url).json()
author = response['by']
title = response['title']
type_of_article = response['type']
try:
    url = response['url']
except:
    url = f'https://news.ycombinator.com/item?id={id_of_post}'

print (author, title, type_of_article, url)

tweet = f"{title} by {author}\nRead more about this {type_of_article} here --> {url}"
api.update_status(tweet)
