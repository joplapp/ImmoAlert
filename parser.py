#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
from sendmail import sendMail
from post import Post
from config import Config

def parse(url, alreadyNotified):
    print("Getting posts from ", url)

    a = requests.get(url).text
    tree = BeautifulSoup(a, "lxml")

    items = tree.find_all('li', attrs={'class': 'result-list__listing'})
    print("Found", len(items)/2, "posts (assuming every 2nd is hidden)")

    sentEmailsCounter = 0
    for item in items:

        # check if this is some hidden post
        hidden = (len(item.get('class')) > 1)
        if hidden:
            continue

        # check if we already covered this post
        id = item.get('data-id')
        try:
            ind = alreadyNotified.index(id)
            continue
        except ValueError:
            justgo="on" # just go on

        # if this post is new, parse it
        post = Post(item)

        sendMail(post)

        logId(id)
        sentEmailsCounter+=1

    print("Sent", sentEmailsCounter, "emails")

DB_LOCATION = 'notified_ids.txt'
def initDb():
    try:
        fo = open(DB_LOCATION, "r+")
        str = fo.read()
        ids = str.split("\n")
    except FileNotFoundError:
        fo = open(DB_LOCATION, "wb")
        ids = []
    finally:
        fo.close()

    return ids

# stores an id in the notified ids file so that no email is sent twice
def logId(postId):
    fo = open(DB_LOCATION, "a")
    fo.write(postId+"\n")
    fo.close()


# actually start everything
alreadyNotified = initDb()
parse(Config.searchUrl, alreadyNotified)