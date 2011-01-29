require 'sinatra'

configure do
  require 'redis'
  uri = URI.parse(ENV["REDISTOGO_URL"])
  REDIS = Redis.new(:host => uri.host, :port => uri.port, :password => uri.password)
end

# access redis within the context of an HTTP request
get '/' do
  "Hello!"
end

get 'database_test' do
  @foos = redis.lrange("foos", 0, -1) # Array
  @foos.inspect
end
