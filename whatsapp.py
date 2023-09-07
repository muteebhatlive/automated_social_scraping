import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
target = input("Enter your value: ")
print('Entered Target is', target)
time.sleep(5)
print('Started')
# Find the <p> element containing the <span> element with a specific class
# xpath_query = '//*[@id="side"]/div[1]/div/div/div[2]/div/div/p'
new_chat = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[3]/div')
new_chat.click()
print(new_chat)
search_box= driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div[1]/div/div[2]/div/div[1]')
print(search_box)
search_box.send_keys(target)
print('1')
time.sleep(20)
chat = driver.find_element(By.CLASS_NAME,'_199zF')
chat.click()
print('2')
time.sleep(4)
profile = driver.find_element(By.XPATH,'//*[@id="main"]/header')
profile.click()
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
print('Parsed Data',soup)
print('done')
time.sleep(3000)

# try:
#     element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[3]/div')
#     element.click()
#     print('3')
#     profile = driver.find_element(By.XPATH, '//*[@id="main"]/header')
#     profile.click()
#     time.sleep(300)
# except Exception as e:
#     print(f"User {target} not found")   

driver.quit()