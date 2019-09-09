import time 
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://chercher.tech")
time.sleep(2)
# Open a new window
# This does not change focus to the new window for the driver.
driver.execute_script("window.open('');")

# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
driver.get("http://stackoverflow.com")

time.sleep(2)

driver.switch_to.window(driver.window_handles[0])
driver.get("http://google.se")

