#!/bin/env python
import snscrape
import os
import pandas as pd
from datetime import date
today = date.today()
end_date = today
from_date = '2022-10-01'
user_name = "sammith130"
user_tweets = "snscrape --format '{content!r}'" + \
    f" twitter-user '{user_name}' > user-tweets.txt"
os.system(user_tweets)
if os.stat("user-tweets.txt").st_size == 0:
    print('No Tweets found')
else:
    df = pd.read_csv('user-tweets.txt', names=['content'])
    for row in df['content'].iteritems():
        print(row)
