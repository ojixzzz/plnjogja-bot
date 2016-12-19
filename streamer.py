import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET 

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            return False

        return True

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

myStream = tweepy.Stream(auth = auth, listener=MyStreamListener())
myStream.filter(track=['#Pemeliharaan'], follow='1038987342', async=True)
