import time 
from selenium import webdriver
youtube_search = input('enter the text to search in youtube: ')
driver = webdriver.Chrome()
driver.get("https://www.youtube.com")
driver.find_element_by_id('search').send_keys(youtube_search)
time.sleep(1)
driver.find_element_by_id('search-icon-legacy').click()