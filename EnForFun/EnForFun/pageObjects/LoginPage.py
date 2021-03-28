from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObjects.Page import Page

class LoginPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        # self.tutorial_element=driver.get

    def click_on_login(self):
        login = self.get_element_by_id(id="id_loginbutton")
        login.click()


    def type_in_email(self,text_to_type):
        email = self.get_element_by_id(id="id_email")
        email.send_keys(text_to_type)

    def type_in_password(self,password_to_type):
        password = self.get_element_by_id(id="id_password")
        password.send_keys(password_to_type)
