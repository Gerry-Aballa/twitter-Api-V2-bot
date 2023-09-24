""" A Twitter bot that posts a tweet everyday at the same time(8AM EAT)"""


import tweepy
import time
import datetime
import keys
import schedule

# Initialize Tweepy
client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

# Get the current date and time
current_date = datetime.date.today()

# Format the date as a string
formatted_date = current_date.strftime("%B, %d, %Y")


def sendPost():
    # Send the tweet
    client.create_tweet(text=f"Hello Python 🐍. It is {formatted_date} today!🚀🚀.\nI am a bot 🤖. Meet me on Github https://github.com/Gerry-Aballa/twitter-Api-V2-bot")

    # Print a message to indicate that the request was successful
    print("Tweet posted successfully")

# Schedule the method to be exectued everday at a set time
schedule.ever().day.at("8:00").do(sendPost)

# Main loop
while True:
    # Checks if scheduler has pending tasks
    schedule.run_pending()

    # Scheduler sleeps for 1 day
    time.sleep(1)