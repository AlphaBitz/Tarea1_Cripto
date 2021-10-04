from selenium import webdriver
import os
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
email = "koberok911@timevod.com"
contraseña = 'Test12345678'
nueva_contraseña = 'Test1234567890'

CHROME_BROWSER = webdriver.Chrome(PATH)
CHROME_BROWSER.get("https://www.trekbikes.com/us/en_US/login/")
CHROME_BROWSER.find_element_by_id("j_username").send_keys(email)
CHROME_BROWSER.find_element_by_id("j_password").send_keys(contraseña)
CHROME_BROWSER.find_element_by_xpath('//button[normalize-space()="Log in"]').click()

CHROME_BROWSER.get("https://www.trekbikes.com/us/en_US/my-account/update-password/")
CHROME_BROWSER.find_element_by_id("currentPassword").send_keys(contraseña)
CHROME_BROWSER.find_element_by_id("newPassword").send_keys(nueva_contraseña)
CHROME_BROWSER.find_element_by_id("checkNewPassword").send_keys(nueva_contraseña)
CHROME_BROWSER.find_element_by_xpath('//button[normalize-space()="Update"]').click()