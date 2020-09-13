import os
import time

import schedule
import tweepy

# def job():
API_KEY = os.environ['TWITTER_API_KEY']
API_SECRET_KEY = os.environ['TWITTER_API_SECRET_KEY']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search_lists = ['#駆け出しエンジニアと繋がりたい', '#今日の積み上げ']
tweet_count = 100

for search in search_lists:
    print('{} を探し中'.format(search))
    search_result = api.search(q=search, count=tweet_count)
    for tweet in search_result:
        tweet_id = tweet.id
        try:
            api.create_favorite(id=tweet_id)
            print('いいねしました')
            time.sleep(3)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# schedule.every().day.at("12:00").do(job)
# schedule.every().day.at("16:30").do(job)
# schedule.every().day.at("17:25").do(job)
# schedule.every().day.at("21:00").do(job)
# schedule.every().day.at("23:00").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
