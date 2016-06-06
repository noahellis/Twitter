from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import matplotlib.pyplot as plt
import re

access_token = "738084753711075329-xO8NmTZx13RXhXhlJupqHq78rJmMUSq"
access_token_secret = "JS3rAsDe9zkd2iPRfoPKWgval82FB04N1cjdafc7UlOrF"
consumer_key = "sHNNBeLy2uoVdNwC387cMBfks"
consumer_secret = "XPM0hJqRapSK2sTvbXyd0STSzbRhWFk3tlJ0SyQShLAmNLIN1Z"

class StdOutListener(StreamListener):

# 	def on_data(self, raw_data):
# 		print (raw_data)
# 		return True
#
# 	def on_error(self, status):
# 		print (status)
#
# if __name__ == "__main__":
# 	listener = StdOutListener()
# 	auth = OAuthHandler(consumer_key, consumer_secret)
# 	auth.set_access_token(access_token, access_token_secret)
# 	stream = Stream(auth, listener)
#
# 	stream.filter(track=['trump', 'sanders', 'clinton'])

	tweets_data_path = './twitter_data.json'

	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
		try:
			tweet = json.loads(line)
			tweets_data.append(tweet)
		except:
			continue
	tweets = pd.DataFrame()


	tweets_by_lang = tweets['lang'].value_counts()



	tweets_by_lang = tweets['lang'].value_counts()
	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Languages', fontsize=15)
	ax.set_ylabel('Number of tweets' , fontsize=15)
	ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
	tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
	plt.show()


	tweets_by_country = tweets['country'].value_counts()

	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Countries', fontsize=15)
	ax.set_ylabel('Number of tweets', fontsize=15)
	ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
	tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
	plt.show()

# def word_in_text(word, text):
