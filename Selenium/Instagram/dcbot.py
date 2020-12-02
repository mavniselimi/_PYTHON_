from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get("https://discord.com/app")
a=input("Giriş işiniz bitince bi tuşa tıklayınız")
gameHub=browser.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[3]/div[6]""")
gameHub.click()
time.sleep(1)
kom=browser.find_element_by_xpath("""//*[@id="channels"]/div/div[4]""")
kom.click()
time.sleep(1)
metinKutu=browser.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]""")
while True:
    metinKutu.send_keys("pls beg")
    time.sleep(40)
