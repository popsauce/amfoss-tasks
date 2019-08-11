require 'mechanize'
 
agent = Mechanize.new

google_url = "http://google.com/search?q=linux"
 
page = agent.get(google_url)
 
search_form = page.form('f')
 
puts search_form.inspect
