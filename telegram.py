import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.get("https://web.telegram.org/a/")
target = input("Enter your value: ")
print('Entered Target is', target)
time.sleep(5)

text_area = driver.find_element(By.ID, "telegram-search-input")
print(text_area)