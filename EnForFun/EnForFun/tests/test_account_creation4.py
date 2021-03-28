import pytest
from accounts.models import User
from accounts.models import UserManager
from pageObjects.NavBar import NavBar
from pageObjects.LoginPage import LoginPage
from django.urls import reverse,resolve

import time


@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        return django_user_model.objects.create_user(**kwargs)
    return make_user


@pytest.mark.django_db
def test_fixture_create_user(live_server,create_user,driver_init,client):
    user = create_user(email=' ', password='bar')
    print("    client=" + str(client))
    print("dir client=" + str(dir(client)))

    client.force_login(user)
    url=live_server.url + reverse('index_lt')
    driver = driver_init
    driver.get(url)

    time.sleep(100)
    #assert user.is_authenticated is True  # <-- this should be False but it's True
    #assert user.is_anonymous is True      # <-- this fails
    #print("User=")
    #print("Full Name=" + str(client.login))
    #assert False

    #assert False

    nav_bar = NavBar(driver)
    login_page = LoginPage(driver)
    nav_bar.click_on_login()
    login_page.type_in_email('foo@bar.com')
    login_page.type_in_password('bar')
    login_page.click_on_login()
    time.sleep(100)


