from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
type(browser)

browser.get('https://poczta.o2.pl/zaloguj')

user_name = browser.find_element_by_name("username")
user_name.send_keys("not_my_real_email")
password_element = browser.find_element_by_name("password")
password_element.send_keys("maslo")

submit = browser.find_element_by_id("login-button")
submit.click()

html = browser.find_element_by_tag_name("html")
html.send_keys(Keys.END)
html.send_keys(Keys.HOME)

browser.refresh()
browser.back()

