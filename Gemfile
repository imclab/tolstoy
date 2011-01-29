# A sample Gemfile
source "http://rubygems.org"

gem "sinatra"
gem "redis"

configure do
  require 'redis'
  uri = URI.parse(ENV["REDISTOGO_URL"])
  REDIS = Redis.new(:host => uri.host, :port => uri.port, :password => uri.password)
end