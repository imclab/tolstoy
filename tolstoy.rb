require 'sinatra'
require 'redis'


# access redis within the context of an HTTP request
get '/' do
  "Well, hello!"
  uri = URI.parse(ENV["REDISTOGO_URL"])
  redis = Redis.new(:host => uri.host, :port => uri.port, :password => uri.password)
  if redis 
    "Redis appears to be working ..."
  else
    "Redis is down"
  end
end