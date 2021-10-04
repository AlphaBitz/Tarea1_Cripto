from selenium import webdriver
import os
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
email = "koberok911@timevod.com"
contraseña = 'Test1234'


CHROME_BROWSER = webdriver.Chrome(PATH)
CHROME_BROWSER.get("https://www.trekbikes.com/us/en_US/login/pw/request/external/")
CHROME_BROWSER.find_element_by_id("email").send_keys(email)
CHROME_BROWSER.find_element_by_xpath('//button[normalize-space()="Send email"]').click()