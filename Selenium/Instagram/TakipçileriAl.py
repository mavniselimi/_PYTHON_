from selenium import webdriver
import time

import logininfo

browser=webdriver.Chrome()
browser.get("https://www.instagram.com")
username=browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input""")
password=browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input""")
username.send_keys(logininfo.username)
password.send_keys(logininfo.password)
