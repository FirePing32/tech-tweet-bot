import requests
from apis import ACCESS_KEY, ACCESS_SECRET, auth, api

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
querystring = {"print":"pretty"}
id_list = "https://hacker-news.firebaseio.com/v0/newstories.json"
response_of_list = requests.request("GET", id_list).json()

id_of_post = response_of_list[0]
print(id_of_post)
url = f"https://hacker-news.firebaseio.com/v0/item/{id_of_post}.json?print=pretty"

response = requests.request("GET", url).json()
try:
    title = response['title']
    try:
        url = response['url']
    except:
        url = f'https://news.ycombinator.com/item?id={id_of_post}'

    print(title, url)

    tweet = f"{title}\n{url}"
    api.update_status(tweet)
except:
    pass