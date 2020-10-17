from selenium import webdriver
import loginInfo
import time
browser=webdriver.Chrome()
browser.get("https://twitter.com/login")
username=browser.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input""")
password=browser.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input""")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)
time.sleep(3)
login=browser.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div""")
login.click()
article=browser.find_elements_by_css_selector(".css-1dbjc4n")
for articles in article:
    print("""****************************""")
    print(articles.text)
#aramayeri=browser.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div""")
#aramayeri.click()
#arama=browser.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input""")
#searchThing="#SapıkCanDündar"
#arama.send_keys(searchThing)
#"""aramaTusu=browser.find_element_by_xpath("""//*[@id="typeaheadDropdown-15"]/div[2]/div[1]/div""")"""
#browser.get("https://twitter.com/search?q=%23"+searchThing+"&src=typed_query")
#arama.send_keys(searchThing)
#time.sleep(10)
#browser.back()
#time.sleep(10)
browser.close()
