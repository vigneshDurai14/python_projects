import time
from getpass import getpass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class multi():
    def multiple_tabs(self):
        no_of_windows = self.driver.window_handles
        #print(len(no_of_windows))
        if len(no_of_windows) >= 1:
            self.driver.execute_script("window.open('');")
            multiple_windows = self.driver.window_handles
            #print(len(multiple_windows))
            self.driver.switch_to_window(self.driver.window_handles[len(multiple_windows)-1])
        
class Test(multi):
    def __init__(self):
        self.driver = webdriver.Chrome()
        print("Browser Opened with google")
        self.driver.get("https://google.com")
        self.google_window = self.driver.current_window_handle
        
    
    def gmail_login(self):
        print("Gmail login")
        username = input("enter your Gmail I'd: ")
        password = getpass('enter your gmail password: ')
        multi.multiple_tabs(self)
        self.driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        self.driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(username)
        self.driver.find_element_by_id('identifierNext').click()
        time.sleep(3)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id('passwordNext').click()
        self.gmail_window = self.driver.current_window_handle
    
    def gmail_logout(self):
        print('logging out gmail')
        self.driver.switch_to_window(self.gmail_window)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div/div[2]/div/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="gb_71"]').click()
    
    def facebook_login(self):
        print("Gmail login")
        username = input("enter your facebook login I'd: ")
        password = getpass('enter your facebook password: ')
        multi.multiple_tabs(self)
        self.driver.get("https://www.facebook.com")
        self.driver.find_element_by_id('email').send_keys(username)
        self.driver.find_element_by_id('pass').send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_id('u_0_a').click()
        self.facebook_window = self.driver.current_window_handle
    
    def facebook_logout(self):
        print('logout facebook')
        self.driver.switch_to_window(self.facebook_window)
        time.sleep(1)
        self.driver.find_element_by_id("userNavigationLabel").click()
        time.sleep(2)
        self.driver.find_element_by_partial_link_text('Log Out').click()
           
    def youtube_search(self):
        print("Opening youtube")
        youtube_search = input('enter the text to search in youtube: ')
        multi.multiple_tabs(self)
        self.driver.get("https://www.youtube.com")
        self.driver.find_element_by_id('search').send_keys(youtube_search)
        time.sleep(1)
        self.driver.find_element_by_id('search-icon-legacy').click()
    
    def open_new_tab(self):
        print("Open new tab for google search ")
        google_search = input('enter the text to search in google: ')
        multi.multiple_tabs(self)
        self.driver.get("https://google.com")   
        self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(google_search)
        self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click() 
    
    def  google_search(self):
        print("search the text in google")
        google_search = input('enter the text to search in google: ')
        self.driver.switch_to_window(self.google_window)
        self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(google_search)
        self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
    
    def close_broswer(self):
        self.driver.quit()
        

D = Test()

print('1 - open google search \n2 - open new tab \n3 - gmail login \n4 - gmail logout \n 5 - facebook login \n6 - facebook logout \n7 youtube search \n8 close the broswer ')

while True:
        try:
            result = int(input("enter an integer :"))
            if result == 1:
                D.google_search()
            elif result == 2:
                D.open_new_tab()
            elif result == 3:
                D.gmail_login()
            elif result == 4:
                D.gmail_logout()
            elif result == 5:
                D.facebook_login()
            elif result == 6:
                D.facebook_logout()
            elif result == 7:
                D.youtube_search()
            elif result == 8:
                D.close_broswer()
                break
        except:
            print("you have enter a string or wrong number, please the integer from 1 to 8. ")
            pass
