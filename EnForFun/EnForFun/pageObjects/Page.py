from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pageObjects.IDMap import IDMap

class Page():

    def __init__(self, driver):
        self.driver = driver
        self.ObjectMap = IDMap()

    def open_page(self, url):
        self.driver = webdriver.Chrome(r"C:\Drivers\chrome\chromedriver.exe")
        self.driver.get(url)

    def close_page(self):
        self.driver.close()

    def get_element_by_id(self, id, timeout=10):
        print("in get element by id")
        try:
            print("id=<%s> timeout=%s" % (id, timeout))
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, id))
            )
        except:
            assert False
        return element

    def get_element_by_class_name(self, class_name, timeout=10):
        print("in get element by class")
        try:
            print("id=<%s> timeout=%s" % (id, timeout))
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name))
            )
        except:
            assert False, "Can't find an element with the '%s' class name in %s" % (class_name,self.driver.current_url)
        return element


