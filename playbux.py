import requests 
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

request = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=10").json()


chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.playbux.co/register")
elem = driver.find_element('name',"email")
elem.send_keys(request[0])
print(request[0].split('@'))
elem.submit()

elem = driver.find_element('name',"password")
elem.send_keys('Zxczxczxc1!')
elem.submit()

elem = driver.find_element('name',"confirmPassword")
elem.send_keys('Zxczxczxc1!')
elem.submit()

driver.find_element("name","agree").click()

driver.find_element(By.XPATH,"/html/body/div[2]/main/form/div[2]/div[1]/div/div[3]/button").click()

time.sleep(15) 
body = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login={0}&domain={1}".format(request[0].split('@')[0],request[0].split('@')[1]))
print("https://www.1secmail.com/api/v1/?action=getMessages&login={0}&domain={1}".format(request[0].split('@')[0],request[0].split('@')[1]))
print(body.text)

print(driver.title)
