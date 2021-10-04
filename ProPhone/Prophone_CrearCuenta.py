from selenium import webdriver
import os
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
email = "koberok911@timevod.com"
contraseña = 'Test123432424#?"!#?$#"$"#&$#'

CHROME_BROWSER = webdriver.Chrome(PATH)
CHROME_BROWSER.get("https://prophonechile.cl/mi-cuenta/")
CHROME_BROWSER.find_element_by_id("reg_email").send_keys(email)
CHROME_BROWSER.find_element_by_id("reg_password").send_keys(contraseña)
CHROME_BROWSER.find_element_by_name("register").click()