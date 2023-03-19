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

# Function to get trending topics
def get_trending_topics(woeid):
    trends = api.get_place_trends(id=woeid)
    trending_topics = [trend["name"] for trend in trends[0]["trends"]]
    return trending_topics

# Replace the WOEID with the desired location's WOEID
# Worldwide WOEID: 1
# Example for United States WOEID: 23424977
woeid = 1

# Get and print trending topics
trending_topics = get_trending_topics(woeid)
print("Trending topics:")
for topic in trending_topics:
    print(topic)
