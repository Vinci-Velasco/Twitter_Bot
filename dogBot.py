#!/usr/bin/env python3
import config
import os
import time
import requests
import tweepy
from multiprocessing import Process 

# Credentials
consumer_key = config.consumer_key
consumer_token = config.consumer_token
access_token = config.access_token
access_token_secret = config.access_token_secret

# Authenticate to twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_token)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

os.chdir("./images")



def save_image():
    # Download dog photo
    # r is an api request
    r = requests.get("https://dog.ceo/api/breed/retriever/golden/images/random")
    r.raise_for_status()
    dog_photo = r.json()["message"]
    dog_res = requests.get(dog_photo)  # request to image spefically
    dog_res.raise_for_status()
    dogImage = open("Dog_Photo.jpg", "wb")
    for chunk in dog_res.iter_content(100000):
        dogImage.write(chunk)
    dogImage.close()

def tweet_loop():
    while True:
        save_image()
        api.update_with_media("Dog_Photo.jpg")
        # Tweet after every hour
        time.sleep(3600)

def reply_loop():
    while True:
        tweets = tweepy.Cursor(api.search, q="I want a dog", result_type="recent", lang="en").items(3)
        for tweet in tweets:
            save_image()
            api.update_with_media("Dog_Photo.jpg", 
            "Here's a dog photo for you! @" + tweet.user.name, tweet.id)
        time.sleep(7200) 

if __name__ == '__main__':
    Process(target=tweet_loop).start()
    Process(target=reply_loop).start()
