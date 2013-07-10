
from selenium import webdriver

b = webdriver.Firefox()
b.get("http://www.gmanetwork.com/news/sports/uaap")
f = b.find_element_by_link_text("Full Story")
f.click()

'''
to-do

extract text and remove html tags 

'''
