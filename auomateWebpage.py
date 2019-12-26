import time

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read for Free')
linkElem.click()
time.sleep(2)
linkElem = browser.find_element_by_link_text('Automate the Boring Stuff with Python')
linkElem.click()