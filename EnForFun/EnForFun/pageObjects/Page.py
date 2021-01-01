from selenium import webdriver



class Page():

    def __init__(self):
        pass

    def openPage(self,url):
        self.driver = webdriver.Chrome("C:\Drivers\chrome\chromedriver.exe")
        self.driver.get(url)

    def closePage(self):
        self.driver.close()
