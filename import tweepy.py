import tweepy
import json 

consumer_key = 'xLGiN7k5eJhijLUJ2JaIpSRUO'
consumer_secret = 'FkKXbLTWQNAdGrZMtN1NQ0sJpe32FzxeFponv9kpyTWMWEn6NH'

access_token = '1546900559826911240-DT4iDWSsjGosmjOqnMQjL1kXduKQpJ'
access_token_secret = '4cT4eI4tQqVapEBYQdSzpwWOgf1rlaK0ZYNSggglx8unY'

bearer_token = r"AAAAAAAAAAAAAAAAAAAAAA8HfAEAAAAAuDjjs5csk2a7LRt%2FqxE9wrPEt0s%3D0EiMBc8r59KldNu31Z8AZxgj8yYYQNYu4Gwj5MTDCduiECOndV"

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in api.home_timeline():
    print(tweet.text)