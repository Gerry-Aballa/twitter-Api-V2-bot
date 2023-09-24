## A Twitter bot that posts a tweet everyday at the same time(8AM EAT)
Meet me on [Twitter](https://twitter.com/HelloPythonBot)

### Requirements
- [Twitter Developer account](https://developer.twitter.com/en)
- [tweepy](https://docs.tweepy.org/en/stable/install.html)
- [requests](https://pypi.org/project/requests/)
- [schedule](https://pypi.org/project/schedule/)

```bash
pip install -r requirements.txt
```

### How it works

#### Step 1: Import the necessary libraries
```python
import tweepy
import time
import datetime
import keys
import schedule
```

#### Step 2: Initialize Tweepy with Twitter API
```python
client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)
```

#### Step 3: Create a method to send the tweet
```python
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
schedule.ever().day.at("8.00").do(sendPost)
```

#### Step 4: Define the main loop
```python
while True:
    # Checks if scheduler has pending tasks
    schedule.run_pending()

    # Scheduler sleeps for 1 day
    time.sleep(1)
```

#### Step 5: Create a keys.py file and add your Twitter API keys
```python
bearer_token = "YOUR_BEARER_TOKEN"
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
```

#### Step 6: Run the bot
```
python3 twitter.py
```