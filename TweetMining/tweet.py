import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'OU4n6gpftucZHbF727ylx6pe3'
consumer_secret = '9G2RBxpTCQwXiUqhLlpvrnj4arzOLTKbAPhEhfSYJQs5Uv0onD'
access_token = '321787319GSH9sxzlA9qsJFp9NnWXu4aBJyjQFy5tIw49LOef'
access_secret = 'n4bub6B82yAfqTgzYm4vQLCb2a0JPas6aGPMtb2gX08Ly'
 
auth = OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
for tweet in api.search(q="jaringan", rpp=100):
	print(tweet.text)
	print('\n')