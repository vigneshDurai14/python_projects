import time 
from selenium import webdriver
from getpass import getpass

username = input("enter the gmail I'd: ")
password = getpass('enter the password: ')
driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Ftab%3Dwm%26ogbl&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(username)
driver.find_element_by_id('identifierNext').click()
time.sleep(3)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_id('passwordNext').click()

time.sleep(10)
driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div/div[2]/div/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="gb_71"]').click()