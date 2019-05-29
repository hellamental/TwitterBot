import tweepy
consumer_key = 'hvuc8cWbLZaGHfklsto4jP0vo'
consumer_secret = 'PiLc2S4psxBOw7steYmtWxucN1KBrAkoaEabYHdMTltJuIgs7r'
access_token = '1048368143461019648-rWCOznHlixxdjURSmCSzpcoiGRYSsc'
access_token_secret = 'mFl3y1ABCxZHeU8OoDEoaNR5Q50YKP3iNM0z0PDHdPRrl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)

def from_creator(status):
    if hasattr(status, 'retweeted_status'):
        return False
    elif status.in_reply_to_status_id != None:
        return False
    elif status.in_reply_to_screen_name != None:
        return False
    elif status.in_reply_to_user_id != None:
        return False
    else:
        return True

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if from_creator(status) == True:
            
            print status.screen_name + str("  ") + ((status.text).encode('utf8'))
        else:
            pass



myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['metoo'])

