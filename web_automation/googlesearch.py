import time 
from selenium import webdriver

google_search = input('enter the text to search in google: ')

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(google_search)

driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()

