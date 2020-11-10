import time
import selenium.webdriver as webdriver
k=97
def get_results(search_term):
    url="https://in.search.yahoo.com/"
    browser=webdriver.Chrome()
    browser.get(url)
    search_box=browser.find_element_by_id("yschsp")
    search_box.send_keys(search_term)
    try:
        link=browser.find_element_by_xpath("//ol[@class='web_regular_results']//h3//a")
    except:
        link=browser.find_element_by_xpath("//h3//a")
    href=link.get_attribute("href")
    print(href)
    browser.close()
    p=open("text1.txt","a")
    z=str(k)
    p.write(z+"->> "+ search_term +"->>"+href+"\n\n")
    p.close()
    return href
f=open("text.txt","r")
for x in f:
    k=k+1
    get_results(x)
