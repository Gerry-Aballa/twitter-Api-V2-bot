""" A Twitter bot that posts a tweet everyday at the same time(8AM EAT)"""


import tweepy
import time
import datetime
import keys


# Initialize Tweepy
client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)


# Main loop
while True:
    # Get the current date and time
    current_date = datetime.date.today()
    current_time = datetime.datetime.now()

    # Format the date as a string
    formatted_date = current_date.strftime("%B, %d, %Y")

    # Define the time at which you want to post the tweet (e.g., 8:00 AM)
    scheduled_time = current_time.replace(hour=8, minute=0, second=0, microsecond=0)

    # Check if the current time is equal to the scheduled time
    if current_time == scheduled_time:

        # Post this tweet if condition is true
        client.create_tweet(text=f"Hello Python 🐍. It is {formatted_date} today!🚀🚀.\nI am a bot 🤖. Meet me on Github https://github.com/Gerry-Aballa/twitter-Api-V2-bot")

        # Wait for 24 hours before checking again
        time.sleep(24 * 3600)  # Sleep for 24 hours
