require 'rubygems'
require 'sinatra'
require 'redis'

if ENV['RACK_ENV'] == 'production'
  uri = URI.parse(ENV["REDISTOGO_URL"])
  REDIS= Redis.new(:host => uri.host, :port => uri.port, :password => uri.password)
else
  REDIS= Redis.new(:host => "localhost", :port => "6379")
end

get '/' do
  REDIS['foo'] = 'bar'
  "Redis appears to be working ..."
end