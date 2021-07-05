#!/usr/bin/python

import praw
from config import *
import os
import random
import time
import re

def bot_login():
    r = praw.Reddit(username = userN,
                    password = userP,
                    client_secret = cSC,
                    client_id = cID,
                    user_agent = userAgent)
    return r
    print("Logged in")
    print(r.user.me())


def run_bot(r, comments_replied_to, WholeWord):
    keyword = ["min", "vision", "foretelling", "viewing", "elmindreda", "farshaw", r.user.me()]
    

    for comment in r.subreddit('Elmindreda_bot').comments(limit = 25):

        commentb = comment.body
        
        
        for key in keyword:
                
            if WholeWord(key)(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            
                with open("Quotes.txt", "r") as f:
                    quote = f.read()
                    quote = quote.split("\n")
##                    quote = filter(None, quote)

                comment.reply(random.choice(quote))

                comments_replied_to.append(comment.id)

                with open("Comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                print("Comment found!")

    print("Sleeping for a bit")
    time.sleep(10)
    

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("Comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")

    return comments_replied_to
            

def WholeWord(w):

    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


r = bot_login()
comments_replied_to = get_saved_comments()


while True:
    run_bot(r, comments_replied_to, WholeWord)
