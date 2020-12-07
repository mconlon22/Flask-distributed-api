import selenium.webdriver as webdriver
import time
import pandas as pd
from numpy import asarray
from numpy import savetxt


def get_results(address, County):
    url = "https://finder.eircode.ie/#/"
    browser = webdriver.Chrome()
    browser.get(url)

    print(browser)
    time.sleep(2)

    search_box = browser.find_element_by_name("searchQuery")

    search_box.send_keys(address+" "+County)
    button = browser.find_element_by_xpath(
        "/html/body/div[2]/div/div[1]/div/div[2]/form/div[1]/span/input")
    button.click()
    time.sleep(2)
    eircode = ""
    if browser.current_url == "https://finder.eircode.ie/#/group-options":
        time.sleep(2)
        try:
            addressButton = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/ul/li[3]/a")
            addressButton.click()
            time.sleep(2)

        except:
            print("straight to eircode page")

    time.sleep(2)     
    
    for i in range(10,0,-1):
        try:
            eircode = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/address-list/div["+str(i)+"]/span")
            
            if len(eircode.text)==8:
                return eircode.text
        except:
            print("trying "+ str(i))




data = pd.read_csv("PPR-ALL.csv", engine='python') 
eircodes = []

county = data["County"]
try:
    values = "couldnt find eircode"
    for x in range(0, 50000):
        print("iteration number: " + str(x))
        try:
            values = get_results(addresses[x], county[x])
            print(values)
            data.insert(x, "Eircode",values)   
        except:
            print(values)


        value = [values, addresses[x]]
        print(value)
    data.to_csv('./out.csv',index=False)

except:
    data.to_csv('./out.csv',index=False)
