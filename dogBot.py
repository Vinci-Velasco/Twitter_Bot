import config
import os
import time
import requests
import tweepy
from multiprocessing import Process 
print(os.getcwd)

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
    r = requests.get
    ("https://dog.ceo/api/breed/retriever-golden/images/random")
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

if __name__ == '__main__':
    Process(target=tweet_loop).start()  """