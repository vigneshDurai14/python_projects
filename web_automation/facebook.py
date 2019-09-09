import time 
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys

username = input("enter your facebook login I'd: ")
password = getpass('enter your facebook password: ')
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="u_0_3"]').click()

time.sleep(10)

driver.find_element_by_id("userNavigationLabel").click()
time.sleep(2)
driver.find_element_by_partial_link_text('Log Out').click()