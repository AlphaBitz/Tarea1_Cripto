from selenium import webdriver
import os
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
email = "koberok911@timevod.com"
contraseña = 'Test123432424#?"!#?$#"$"#&$#'
nueva_contraseña = 'Test1234567890&%/$&$#$!"'


CHROME_BROWSER = webdriver.Chrome(PATH)
CHROME_BROWSER.get("https://prophonechile.cl/mi-cuenta/")
CHROME_BROWSER.find_element_by_id("username").send_keys(email)
CHROME_BROWSER.find_element_by_id("password").send_keys(contraseña)
CHROME_BROWSER.find_element_by_name("login").click()  

CHROME_BROWSER.get("https://prophonechile.cl/mi-cuenta/edit-account/")
CHROME_BROWSER.find_element_by_id("account_first_name").clear()
CHROME_BROWSER.find_element_by_id("account_first_name").send_keys("FN")
CHROME_BROWSER.find_element_by_id("account_last_name").clear()
CHROME_BROWSER.find_element_by_id("account_last_name").send_keys("LN")
CHROME_BROWSER.find_element_by_id("account_display_name").clear()
CHROME_BROWSER.find_element_by_id("account_display_name").send_keys("Koberok1990")
CHROME_BROWSER.find_element_by_id("password_current").send_keys(contraseña)
CHROME_BROWSER.find_element_by_id("password_1").send_keys(nueva_contraseña)
CHROME_BROWSER.find_element_by_id("password_2").send_keys(nueva_contraseña)
CHROME_BROWSER.find_element_by_name("save_account_details").click()