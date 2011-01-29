import json
import marshal
import redis

# define the token limits
min_tokens = 3
max_tokens = 3

# connect to the database
rdb = redis.Redis(host='localhost', port=6379, db=1)

# delete previous key if it exists
rdb.delete('substrings')

# get all of the tweet ids
tids = rdb.hkeys('tweets')

# for each tweet...
i = 0
for tid in tids:

    # load the tweet
    tweet = json.loads(rdb.hget('tweets',tid))
    
    # split the text on whitespace
    tokens = tweet['text'].split(' ')
    
    # while there are at least the minimum number of tokens available...
    while len(tokens) >= min_tokens:
    
        # index using every possible substring up to min( max_tokens, len(tokens) )
        for j in range(min_tokens,min(max_tokens,len(tokens))+1,1):
        
            # construct the substring
            substring = marshal.dumps(tokens[:j])
            
            # index the tweet based on the substring
            if rdb.hexists('substrings',substring):
           
                # get the current list of tweet ids
                tids = marshal.loads(rdb.hget('substrings',substring))
                
                # add the tweet id
                tids.append(tweet['id'])
                
            else:
            
                # add the initial list
                tids = [tweet['id']]
                
            # push the list to the database
            rdb.hset('substrings',substring,marshal.dumps(tids))
    
        # remove the first token in the token list
        tokens = tokens[1:]
        
    i += 1
    if i % 100 == 0:
        print "%d tweets processed." % i        
