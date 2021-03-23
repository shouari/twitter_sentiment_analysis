import twint
import nest_asyncio
 # refer to Twint documentation for further details ; https://github.com/twintproject/twint
nest_asyncio.apply()
t = twint.Config()

t.Search = "keyword"
t.Store_object = True
t.Limit = 25000
t.Store_csv = True
t.Output = "tweets_extracted"
twint.run.Search(t)


