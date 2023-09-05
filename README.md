## A Twitter bot that posts a tweet everyday at the same time(8AM EAT)
Meet me on [Twitter](https://twitter.com/HelloPythonBot)


### How it works

### Step 1: Import the necessary libraries
```python
import tweepy
import time
import datetime
import keys
```

### Step 2: Initialize Tweepy
```python
client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)
```

### Step 3: Define the main loop
```python
while True:
    # Get the current date and time
    current_date = datetime.date.today()
    current_time = datetime.now()

    # Format the date as a string
    formatted_date = current_date.strftime("%B, %d, %Y")

    # Define the time at which you want to post the tweet (e.g., 8:00 AM)
    scheduled_time = current_time.replace(hour=8, minute=0, second=0, microsecond=0)

    # Check if the current time is equal to the scheduled time
    if current_time == scheduled_time:

        # Post this tweet if condition is true
        client.create_tweet(text="Hello Python 🐍. It is {formatted_date} today!🚀🚀.\nI am a bot 🤖. Meet me on https://github.com/Gerry-Aballa/twitter-Api-V2-bot")

        # Wait for 24 hours before checking again
        time.sleep(24 * 3600)  # Sleep for 24 hours
```

### Step 4: Create a keys.py file and add your Twitter API keys
```python
bearer_token = "YOUR_BEARER_TOKEN"
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
```

### Step 5: Run the bot
```
python twitter.py
```