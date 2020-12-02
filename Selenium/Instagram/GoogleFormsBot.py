from selenium import webdriver
import time
import random
browser=webdriver.Chrome()
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSc1S8bUtx09olsyOyBEwmLf1mgMvU5tNGiGyTV1o9gF8XkUvg/viewform")
time.sleep(1)
eposta=browser.find_element_by_xpath("""//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input""")
eposta.send_keys("1love@mevall.com")
kullaniciadi=browser.find_element_by_xpath("""//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input""")
kullaniciadi.send_keys("Bip Bop I am a bot")
eposta2=browser.find_element_by_xpath("""//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input""")
eposta2.send_keys("1love@mevall.com")
tel=browser.find_element_by_xpath("""//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input""")
tel.send_keys("202-555-0906")
schoolinfo=browser.find_element_by_xpath("""//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input""")
schoolinfo.send_keys("Nowhere i am a bot bip bop")
array=[browser.find_element_by_xpath("""//*[@id="i26"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i29"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i29"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i32"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i35"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i38"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i41"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i44"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i47"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i50"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i53"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i56"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i59"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i62"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i65"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i68"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i71"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i74"]/div[2]"""),browser.find_element_by_xpath("""//*[@id="i77"]/div[2]""")]
a=random.randint(1,18)
array[a].click()
b=random.randint(1,18)
while a==b:
    b=random.randint(1,18)
array[b].click()
textarea=browser.find_element_by_xpath("""//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea""")
textarea.send_keys("Bip bop i am a bot")
button=browser.find_element_by_xpath("""//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span""")
c=input("Do you wanna send form?(Y/N)")
if c=="y" or c=="Y":
    button.click()
    time.sleep(1)
    print("File send successfully")
    browser.quit()
    exit(1)
else:
    print("Good Days!")
    browser.quit()
    exit(1)
