import sys
sys.path.append("..")
from pageObjects.LoginPage import LoginPage
import pytest
from selenium import webdriver

# Fixture for Chrome
@pytest.fixture(scope="module")
def driver_init(request):
    print("Chrome_driver_init")
    chrome_driver = webdriver.Chrome("C:\Drivers\chrome\87.0.4280.20\chromedriver.exe")
    #request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


# def login_setup():
#     print('Setup for login called')

# def login_teardown():
#     print('Teardown for login called')


# def setup_module(module):
#     print('\nSetup of module is called')


# def teardown_module(module):
#     print('\nTeardown of module is called')

@pytest.mark.usefixtures("driver_init")
def test_login(module):
    print("<<Test_login")
    chrome_driver.get("http://127.0.0.1:8000/login/")

def test_login2():
    print("<<Test_login2")

