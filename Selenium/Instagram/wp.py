from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://goo.gl/WCS3hC")
wait = WebDriverWait(driver, 600)
driver.maximize_window()
wait = WebDriverWait(driver, 600)
input("Kare Kod okuttuktan sonra Enter'a basınız.")
aramayeri=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
h=input("Yazmak İstediğiniz grubu Veya Kişiyi tam haliyle yazınız yazınız")
aramayeri.send_keys(h)
time.sleep(2)
grup = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[4]')
grup.click()
time.sleep(2)
i="a"
box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
while i!="":
    i=input("Mesajınızı Giriniz")
    box.send_keys(i)
    time.sleep(1)
    button=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    button.click()
exit(1)