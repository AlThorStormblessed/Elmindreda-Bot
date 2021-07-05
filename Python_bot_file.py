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
    keyword = ["min", "vision", "foretelling", "viewing", "elmindreda", "farshaw", r.user.me(), "viewings", "visions"]


    for comment in r.subreddit('Elmindreda_bot').comments(limit = 25):

        if WholeWord("rand")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            rand_quotes = [
                "I like older men. I like men with education, and wit. I have no interest in farms, or sheep, or shepherds. But then, you aren't a shepherd, are you? Not anymore. Light, why did the Pattern have to catch me up with you? Why couldn't I have something safe and simple, like being shipwrecked with no food and a dozen hungry Aielmen?",
                "I'm bound to him as surely as a stave is bound to the barrel. But I can't see if he'll ever love me in return. And I am not the only one.",
                "You have me, looby.",
                "Burn you, Rand al'Thor!",
                "Woolheaded sheepherder!",
                "*Boink*",
                "Men are strange. I think it has something to do with the hair on their chins.",
                "I want to get drunk as a drowned mouse, and fast!",
                "Fall in love with a man, and you end up doing laundry, even if it does belong to another man.",
                "Rand, don't look at me like that. I am on your side, if it comes to sides. It might; a little. They think I'll tell them what you say. I won't, Rand. They just want to know how to deal with you, what to expect, but I'll not tell one word you don't want me to, and if you ask me to lie, I will. They do not know about my viewings. Those are yours, Rand. You know I will read anyone you say, including Merana and the rest."]

            comment.reply(random.choice(rand_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

        elif WholeWord("thom")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            thom_quotes = [
                "Go juggle something, Thom",
                "Men are strange. I think it has something to do with the hair on their chins."]

            comment.reply(random.choice(thom_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

        elif WholeWord("perrin")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            perrin_quotes = [
                "If you meet a woman – the most beautiful woman you’ve ever seen – run!",
                "Men are strange. I think it has something to do with the hair on their chins."]

            comment.reply(random.choice(perrin_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

        elif WholeWord("toh")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            toh_quotes = [
                "I don’t know what anybody’s toes have to do with anything, or feet either, but I’m not going anywhere until you talk to them, Rand!"]

            comment.reply(random.choice(toh_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

        elif WholeWord("egwene")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            egwene_quotes = [
                "I am no novice. Yes, Aes Sedai. No, Aes Sedai. May I sweep another floor, Aes Sedai?",
                ]

            comment.reply(random.choice(egwene_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

        elif WholeWord("gawyn")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            gawyn_quotes = [
                "Gawyn, you know me. You can't think I would help the Black Ajah. Gawyn, Elayne supports her and everything she's done. Your own sister, Gawyn. Egwene believe in her too, Gawyn. I swear it, Gawyn. Egwene believes.",
                "I fear I know little of books my Lord Gawyn. I always mean to read one – I do. But there is so little time. Why, just fixing my hair properly takes hours. Do you think it is pretty?",
                ]

            comment.reply(random.choice(gawyn_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

        elif WholeWord("aviendha")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            aviendha_quotes = [
                "I don’t know what anybody’s toes have to do with anything, or feet either, but I’m not going anywhere until you talk to them, Rand!",
                "Could we go find that oosquai, now? I want to get drunk as a drowned mouse, and fast!",
                ]

            comment.reply(random.choice(aviendha_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

        else:
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
    time.sleep(120)  #Two minute cool-down period

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
