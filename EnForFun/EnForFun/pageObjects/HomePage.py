from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

driver = webdriver.Chrome("C:\Drivers\chrome\chromedriver.exe")
driver.get("http://127.0.0.1:8000/languageTests/")
element = driver.find_element_by_id("homePage")
print(element)
driver.close()
