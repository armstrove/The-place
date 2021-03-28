import sys
sys.path.append("..")
from pageObjects.LoginPage import LoginPage
from pageObjects.NavBar import NavBar
import pytest
from selenium import webdriver
import time

@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        return django_user_model.objects.create_user(**kwargs)
    return make_user

@pytest.mark.django_db
def authenticated_user(client, django_user_model):
    email       = "some@gmail.com",
    password    = "Bobo!@34",
    full_name   = "Vazgen",
    is_active      = True,
    is_staff       = False,
    is_admin       = False,
    user = django_user_model.objects.create_user(
       email       = "some@gmail.com",
       password    = "Bobo!@34",
       full_name   = "Vazgen",
       is_active      = True,
       is_staff       = False,
       is_admin       = False,
   )

@pytest.mark.django_db
def test_login(driver_init):
    driver = driver_init
    navbar = NavBar(driver)
    page   = LoginPage(driver)
    navbar.click_on_login()
    page.type_in_email("some@gmail.com")
    page.type_in_password("Bobo!@34")
    page.click_on_login()

    time.sleep(20)






