from selenium import webdriver
import os
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
email = "koberok911@timevod.com"
contraseña = 'Test1234'

CHROME_BROWSER = webdriver.Chrome(PATH)
CHROME_BROWSER.get("https://www.trekbikes.com/us/en_US/login/")
CHROME_BROWSER.find_element_by_id("firstName").send_keys("Nombre")
CHROME_BROWSER.find_element_by_id("lastName").send_keys("Apellido")
CHROME_BROWSER.find_element_by_id("email").send_keys(email)
CHROME_BROWSER.find_element_by_id("password").send_keys(contraseña)
CHROME_BROWSER.find_element_by_id("registerPasswordConfirmation").send_keys(contraseña)
CHROME_BROWSER.find_element_by_xpath('//button[normalize-space()="Create an account"]').click()