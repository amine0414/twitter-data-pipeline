import tweepy
import pandas as pd
import json
from datetime import datetime
access_key="VCECcrQ4l7tzxyMcfGX2VI6Rt"
access_secret="eI1AcMoUUXJDHd6EJ5wLCJPYaCnKcxSEE8WbfrWMnBcjI7PRgh"
consumer_key="1584671143075643397-teLOXP28ctniR0I4Jj9Ylh1GEPRcyS"
consumer_scret="r2HRq888dC2ZkSetiHpdT8fGC7o8LFA20hF9mEIvVYhrS"

auth=tweepy.OAuthHandler(access_key,access_secret)
auth.set_access_token(consumer_key,consumer_scret)

api=tweepy.API(auth)
tweets=api.user_timeline(screen_name='@elonmusk',
                                   count=200,
                                    include_rts=False,
                                    tweet_mode='extended'  
                                   )
  
tweet_list=[]
for tweet in tweets:
    text=tweet._json["full_text"]
    another_tweet={
        "user":tweet.user.screen_name,
        "text":text,
        "favorite_count":tweet.favorite_count,
         "retweet_count":tweet.retweet_count,
         "created_at":tweet.created_at
    }
    tweet_list.append(another_tweet)  
df=pd.DataFrame(tweet_list)
df.to_csv("Tweetdata.csv")                                 