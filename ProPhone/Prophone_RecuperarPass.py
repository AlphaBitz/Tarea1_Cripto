from selenium import webdriver
import os
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
email = "koberok911@timevod.com"



CHROME_BROWSER = webdriver.Chrome(PATH)
CHROME_BROWSER.get("https://prophonechile.cl/mi-cuenta/lost-password/")
CHROME_BROWSER.find_element_by_id("user_login").send_keys(email)
CHROME_BROWSER.find_element_by_xpath('//button[normalize-space()="Restablecer contraseña"]').click()

