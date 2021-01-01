from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObjects.Page import Page

class LoginPage(Page):

     def __init__(self):
         pass

     def setup(self):
         self.openPage("http://127.0.0.1:8000/login/")

     def login(self,username,password):
         print(self.driver)


