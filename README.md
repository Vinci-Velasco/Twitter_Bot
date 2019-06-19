# Twitter_Bot
Twitter bot that tweets golden retrievers!

How it works (dogbot.py):
  - Authenticate to twitter 
  - Create two processes
    - First process: downloads image from dog API
      and tweets it hourly
    - Second process: When someones tweet has the phrase "I want a dog",
      an image is downloaded and is tweeted @ that person. This occurs to
      3 people every 2 hours (So people don't get annoyed of spam)
      
Getting Started:
  - Clone the repo
  - Create your own config.py with variables of your twitter api tokens
