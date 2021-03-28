import pytest
from selenium import webdriver
from django.core.management import call_command

@pytest.fixture(params=["chrome"],scope="session")
def driver_init(request):
     if request.param == "chrome":
         web_driver = webdriver.Chrome(r"C:\Drivers\chrome\chromedriver.exe")
     if request.param == "firefox":
         binary = FirefoxBinary()
         web_driver = webdriver.Firefox(firefox_binary=binary)
     yield web_driver
     web_driver.close()

@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'my_fixtures.json')


