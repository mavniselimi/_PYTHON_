from selenium import webdriver
import time as zaman
import random
browser = webdriver.Chrome()
entries=[]
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
for a in range(1,10):
    f=random.randint(1,1290)
    browser.get(url+str(f))
    elements=browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    elements=[]
elemanssayısı=len(entries)
a=1
with open("entries.txt","w",encoding="UTF-8") as file:
    for entry in entries:
        file.write("\n*********************************\n")
        file.write(str(a)+".\n"+entry)
        a+=1
zaman.sleep(5)
browser.close()
