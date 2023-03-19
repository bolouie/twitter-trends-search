# Twitter Trending Topics and Search Scraper

This repository contains Python code to scrape trending topics and search for tweets related to a specific topic using the Twitter API and the Tweepy library.

## Prerequisites

- Python 3.x
- A Twitter Developer Account with API access
- Tweepy library installed

## Installation

1. Clone the repository:
`git close http://github.com/bolouie/twitter-trends-search.git`


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




