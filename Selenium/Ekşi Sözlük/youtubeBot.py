from selenium import webdriver
import time as zaman
i=0
while True:
    browser = webdriver.Chrome()
    url = "https://www.youtube.com/watch?v=ytUxIxSDzc8"
    browser.get(url)
    i+=1
    print(i)
    zaman.sleep(2)
    browser.close()
