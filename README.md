# Twitter Trending Topics and Search Scraper

This repository contains Python code to scrape trending topics and search for tweets related to a specific topic using the Twitter API and the Tweepy library.

## Prerequisites

- Python 3.x
- A Twitter Developer Account with API access
- Tweepy library installed

## Create a Twitter Developer Account: 
To use the Twitter API to scrape trending topics, you'll first need to create a developer account, 
obtain the necessary API keys, and install the Tweepy library to interact with the API in Python. 
- Go to https://developer.twitter.com/ and sign in with your Twitter account.
- Apply for a developer account by following the prompts and filling out the required information.
- Once your account is approved, go to the "Projects & Apps" section and create a new project.
- Create a new app inside the project and take note of the API key, API key secret, access token, and access token secret. You'll need these credentials to interact with the API.



## Installation

1. Clone the repository:
`git clone https://github.com/bolouie/twitter-trends-search.git`


2. Install the Tweepy library:
`pip install tweepy`


## Configuration

Replace the placeholder values for `API_KEY`, `API_SECRET`, `ACCESS_TOKEN`, and `ACCESS_SECRET` in the Python scripts with your own Twitter API credentials.

## Usage

### Trending Topics

To fetch and display trending topics, run the `trending_topics.py` script:

You can change the `woeid` variable in the script to get trends for a specific location.

### Search Tweets

To search for tweets related to a specific topic, run the `search_tweets.py` script:

You can adjust the `query` variable in the script to search for different topics and modify the `count` variable to fetch a different number of tweets (up to 100 per request).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




