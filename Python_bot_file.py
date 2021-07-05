#!/usr/bin/python

import praw
from config import *
import os
import random
import time
import re

#Bot login
def bot_login():
    r = praw.Reddit(username = userN,
                    password = userP,
                    client_secret = cSC,
                    client_id = cID,
                    user_agent = userAgent)
    return r
#    print("Logged in")
#    print(r.user.me())


def run_bot(r, comments_replied_to, WholeWord):
    #Keywords that the bot replies to
    keyword = ["min", "vision", "foretelling", "viewing", "elmindreda", "farshaw", r.user.me()]


    for comment in r.subreddit('Elmindreda_bot').comments(limit = 25):

        for key in keyword:

            #Searching for keywords and making sure it isn't in the "replied to" list
            if WholeWord(key)(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():

                #Opening Quotes.txt, where all the bot quotes are saved
                with open("Quotes.txt", "r", encoding='cp1252') as f:
                    quote = f.read()
                    quote = quote.split("\n")

                comment.reply(random.choice(quote)) #Chooses a random quote from Quotes.txt

                comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")

    print("Sleeping for a bit")
    time.sleep(300)  #Five minute cool-down period

#Function to save comments replied to
def get_saved_comments():

    if not os.path.isfile("comments_replied_to.txt"):

        comments_replied_to = []

    else:

        with open("Comments_replied_to.txt", "r", encoding='cp1252') as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")

    return comments_replied_to

#Splits comment replied to into whole words
def WholeWord(w):

    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

#Running the functions
r = bot_login()
comments_replied_to = get_saved_comments()


while True:
    run_bot(r, comments_replied_to, WholeWord)
