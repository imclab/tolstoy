import marshal
import redis

# connect to the database
rdb = redis.Redis(host='localhost', port=6379, db=1)

def top_n_substrings(n):

    # pull the top n substrings from redis, unmarshal them and join tokens into
    # a single string
    return map(' '.join,map(marshal.loads,rdb.zrange('sorted_substrings',1,n,desc=True)))
    