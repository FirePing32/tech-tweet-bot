from os import environ
import time
import sys
import requests
import json
import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler

from api import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET, auth, api

sched = BlockingScheduler()
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

@sched.scheduled_job('interval', minutes=120)
def tweeter():

    querystring = {"print":"pretty"}

    headers = {
        'x-rapidapi-host': environ['x-rapidapi-host'],
        'x-rapidapi-key': environ['x-rapidapi-key']
        }

    id_list = "https://hacker-news.firebaseio.com/v0/newstories.json"    

    response_of_list = requests.request("GET", id_list, headers=headers, params=querystring).json()

    id_of_post = response_of_list[0]
    print(id_of_post)
    url = "https://community-hacker-news-v1.p.rapidapi.com/item/{postid}.json".format(postid = id_of_post)

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    author = response['by']
    title = response['title']
    type_of_article = response['type']
    url = response['url']

    print (author, title, type_of_article, url)

    tweet = "'{title}' by {author}\nRead more about this {type} here ↓↓ {url}\n\n\nMade with ♥ by @PrakharGurunani".format(title = title, author = author, type = type_of_article, url = url)

    api.update_status(tweet)

sched.start()
