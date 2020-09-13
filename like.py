import time

import schedule
import settings
import tweepy


def job():
    API_KEY = settings.API_KEY
    API_SECRET_KEY = settings.API_SECRET_KEY
    ACCESS_TOKEN = settings.ACCESS_TOKEN
    ACCESS_TOKEN_SECRET = settings.ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    search_lists = ['#駆け出しエンジニアと繋がりたい', '#プログラミング初心者']
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

schedule.every().day.at("9:00").do(job)
schedule.every().day.at("14:00").do(job)
schedule.every().day.at("18:00").do(job)
schedule.every().day.at("23:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
