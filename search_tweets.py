# If you want to search Twitter for tweets related to "futures of education"
# you can use the Tweepy library to access the Twitter API's search functionality. 
# Here's an example of how you can do this:

import tweepy

# Replace these with your own API keys and access tokens
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

# Authenticate with the API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Function to search tweets
def search_tweets(query, count=10):
    tweets = api.search_tweets(q=query, count=count)
    return tweets

# Search query
query = "futures of education"

# Number of tweets to fetch (maximum 100 per request)
count = 10

# Search and print tweets
tweets = search_tweets(query, count)
for tweet in tweets:
    print(f"{tweet.user.screen_name}: {tweet.text}\n")
