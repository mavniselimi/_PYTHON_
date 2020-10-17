from selenium import webdriver
import time as zaman
browser = webdriver.Chrome()
url = "https://en.onlinesoccermanager.com/Login?nextUrl=%2FLogin"
browser.get(url)
checkbutton=browser.find_element_by_xpath("""//*[@id="page-privacynotice"]/div/div/div/div[2]/div[2]/div[2]/div/div/div/label/p""")
checkbutton.click()
Contunie=browser.find_element_by_css_selector(""".btn-new""")
Contunie.click()
devamke=browser.find_element_by_name("login-link")
devamke.click()
kullaniciadia="""//*[@id="manager-name"]"""
sifrea="""//*[@id="password"]"""
LogInButtona="""//*[@id="login"]/span"""
kullaniciadi=browser.find_elements_by_xpath(kullaniciadia)
sifre=browser.find_elements_by_xpath(sifrea)
sifrem=input("Lütfen OSM kullanici adinizi giriniz")
kullaniciadim=input("Lütfen OSM kullanici adinizi giriniz")
kullaniciadi.send_keys(kullaniciadim)
sifre.send_keys(sifrem)
zaman.sleep(1)
LogInButtona.click()
browser.close()

