import snscrape.modules.twitter as sntwitter
import pandas as pd
import json

query = "drive.google.com"
limit = 10
tweets = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
   if len(tweets) == limit:
       break
   else:
       tweets.append([tweet.content, [{'url': link.url} for link in tweet.links]])
       
print(tweets)

df = pd.DataFrame(tweets, columns=['content', 'links'])

with open('tweetsDrive.json', 'w', encoding='utf-8') as json_file:
    json.dump(df.to_dict(orient='records'), json_file, indent=2, ensure_ascii=False)






