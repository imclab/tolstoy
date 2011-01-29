import json
import redis

# connect to the database
rdb = redis.Redis(host='localhost', port=6379, db=1)

# delete previous key if it exists
rdb.delete('tweets')

# open the data file containing the json dump
f = open('earthquake','r')

# read in all of the lines
tweet_strings = f.readlines()

i = 0
for tweet_string in tweet_strings:

    # push tweet into the tweets hash table
    try:
        tweet = json.loads(tweet_string)
    except:
        print "Problematic tweet: %s" % tweet_string
    else:
        rdb.hset('tweets',str(tweet['id']),json.dumps(tweet))
    
    i += 1
    if i % 500 == 0:
        print "%d tweets processed." % i
