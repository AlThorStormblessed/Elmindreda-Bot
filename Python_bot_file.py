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


    for comment in r.subreddit('WetlanderHumor').comments(limit = 25):
#special case of Rand and Perrin mentioned at once.
        elif WholeWord("rand")(comment.body) and WholeWord("perrin")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            wolfAndDragon_quotes = [
                "When you two were together, I saw those fireflies and the darkness stronger than ever...",
                "Twice he's going to have to be there, or you... If he's not, something bad will happen to you. Very bad."
            ]
            comment.reply(random.choice(wolfAndDragon_quotes)) #Chooses a random quote from above list

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")
        
#special case of all 3 boys being mentioned at once.
        elif WholeWord("rand")(comment.body) and WholeWord("perrin")(comment.body) and WholeWord("mat")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            three_amigos_quotes = [
                "Sparks swirling around you, thousands of them, and a big shadow, darker than midnight. The sparks are trying to fill the shadow, and the shadow is trying to swallow the sparks. You are all tied together in something dangerous."]

            comment.reply(random.choice(three_amigos_quotes)) #Chooses a random quote from above list

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")
#rand
        if WholeWord("rand")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            rand_quotes = [
                "Why couldn't I have something safe and simple, like being shipwrecked with no food and a dozen hungry Aielmen?",
                "I'm bound to him as surely as a stave is bound to the barrel. But I can't see if he'll ever love me in return. And I am not the only one.",
                "You have me, looby.",
                "Burn you, Rand al'Thor!",
                "Woolheaded sheepherder!",
                "*Boink*"
                "Men are strange. I think it has something to do with the hair on their chins.",
                "I want to get drunk as a drowned mouse, and fast!",
                "Rand, don't look at me like that. I am on your side, if it comes to sides.",
                "Fall in love with a man, and you end up doing laundry, even if it does belong to another man.",
                "He would almost certainly fail without a woman who was dead and gone...",
                "Fireflies consumed in darkness."
            ]

            comment.reply(random.choice(rand_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

 #perrin
        elif WholeWord("perrin")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            perrin_quotes = [
                "If you meet a woman – the most beautiful woman you’ve ever seen – run!",
                "Men are strange. I think it has something to do with the hair on their chins.",
                "A wolf, and a broken crown, and trees flowering all around Perrin.",
                "An Aielman in a cage. A Tuatha'an with a sword. A falcon and a hawk, perching on your shoulders. Both female, I think",
                "He's found his falcon, and I wouldn't be surprised if she kills him when the hawk appears."
                ]

            comment.reply(random.choice(perrin_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

 #mat
        elif WholeWord("mat")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            mat_quotes = [
                "A red eagle, an eye on a balance scale, a dagger with a ruby, a horn, and a laughing face.",
                "Men are strange. I think it has something to do with the hair on their chins.",

                ]

            comment.reply(random.choice(mat_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

#thom
        elif WholeWord("thom")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            thom_quotes = [
                "Go juggle something, Thom",
                "Men are strange. I think it has something to do with the hair on their chins.",
                "A man — not him — juggling fire, and the White Tower."
                ]

            comment.reply(random.choice(thom_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

#toh
        elif WholeWord("toh")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            toh_quotes = [
                "I don’t know what anybody’s toes have to do with anything, or feet either, but I’m not going anywhere until you talk to them, Rand!"]

            comment.reply(random.choice(toh_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")
#gawyn
        elif WholeWord("gawyn")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            gawyn_quotes = [
                "Gawyn, you know me. You can't think I would help the Black Ajah. Gawyn, Elayne supports her and everything she's done. Your own sister, Gawyn. Egwene believe in her too, Gawyn. I swear it, Gawyn. Egwene believes.",
                "I fear I know little of books my Lord Gawyn. I always mean to read one – I do. But there is so little time. Why, just fixing my hair properly takes hours. Do you think it is pretty?"
                ]

            comment.reply(random.choice(gawyn_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

 #special case of all 3 rand-y ones being mentioned at once. (Min, Elayne, Aviendha) Min is represented by 'min' as well as 'you' (since the bot is Min)
        elif WholeWord("you")(comment.body) and WholeWord("elayne")(comment.body) and WholeWord("aviendha")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me() or WholeWord("min")(comment.body) and WholeWord("elayne")(comment.body) and WholeWord("aviendha")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            three_randyones_quotes = [
                "Two. Two others. And....And I'm one.",
                "Three women before a pyre."
                ]

            comment.reply(random.choice(three_randyones_quotes)) #Chooses a random quote from above list

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

 #egwene
        elif WholeWord("egwene")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            egwene_quotes = [
                "I am no novice. Yes, Aes Sedai. No, Aes Sedai. May I sweep another floor, Aes Sedai?",
                "A white flame and other things."
                ]

            comment.reply(random.choice(egwene_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")
 #aviendha
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
  #elayne
        elif WholeWord("elayne")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            elayne_quotes = [
                "She will have to share her husband with two other women and she will be a queen. A severed hand, not hers.",
                "... and above Elayne's, a red hot iron and an axe."
                ]

            comment.reply(random.choice(elayne_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")
#nynaeve
        elif WholeWord("nynaeve")(comment.body) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            nynaeve_quotes = [
                "A man's ring of heavy gold floated above Nynaeve's head",
                "Nynaeve knelt over someone's corpse in a posture of grief."
                ]

            comment.reply(random.choice(nynaeve_quotes)) #Chooses a random quote

            comments_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("Comments_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


            print("Comment found!")

#Herid Fel
        elif (WholeWord("herid")(comment.body) or WholeWord("fel")(comment.body)) and comment.id not in comments_replied_to and not comment.author == r.user.me():
            fel_quotes = [
                "***Too pretty for Master Fel***"
                ]

            comment.reply(random.choice(fel_quotes)) #Chooses a random quote

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
    time.sleep(30)  #Two minute cool-down period

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
