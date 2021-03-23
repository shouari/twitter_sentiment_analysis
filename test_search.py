import twint
import nest_asyncio

nest_asyncio.apply()
t = twint.Config()

t.Search = "GoRafeeq"
t.Store_object = True
t.Limit = 25000
t.Store_csv = True
t.Output = "tweets_extracted"
twint.run.Search(t)
# tlist = t.search_tweet_list
# print(tlist)

