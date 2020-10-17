#//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div/label/div/div[1]/div[2]
#//*[@id="mG61Hd"]/div/div/div[3]/div/div/div/span/span
from selenium import webdriver
import time as zaman
import random
browser = webdriver.Chrome()
entries=[]
url = "https://docs.google.com/forms/d/e/1FAIpQLSc6ZSFUutTmOD8L4ksTjrGsnRTocZmJbf1KuSWqPEV12Ze2SQ/viewform"
for a in range(1,400):
    browser.get(url)
    elements=browser.find_element_by_xpath("""//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div/label/div/div[1]/div[2]""")
    elements.click()
    k=browser.find_element_by_xpath("""//*[@id="mG61Hd"]/div/div/div[3]/div/div/div/span/span""")
    k.click()
    zaman.sleep(1)
    a=browser.find_element_by_xpath("""/html/body/div[1]/div[2]/div[1]/div/div[4]/a""")
    a.click()
browser.close()
