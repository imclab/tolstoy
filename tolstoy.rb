require 'rubygems'
require 'sinatra'
require 'redis'

uri = URI.parse(ENV["REDISTOGO_URL"])
REDIS= Redis.new(:host => uri.host, :port => uri.port, :password => uri.password)

get '/' do
  haml :index
end