import json
import marshal
import redis

# connect to the database
rdb = redis.Redis(host='localhost', port=6379, db=1)

# get all indexed substrings
substrings = rdb.hkeys('substrings')

i = 0
for substring in substrings:

    # get the list of tweet ids for the substring
    tids = marshal.loads(rdb.hget('substrings',substring))
    
    # push substring and count into the sorted set
    rdb.zadd('sorted_substrings',substring,len(tids))
    
    i += 1
    if i % 100 == 0:
        print "%d substrings processed." % i      
