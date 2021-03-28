import pytest
from accounts.models import User
from accounts.models import UserManager
from pageObjects.NavBar import NavBar
from pageObjects.LoginPage import LoginPage

import time


@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        return django_user_model.objects.create_user(**kwargs)
    return make_user


@pytest.mark.django_db
def test_fixture_create_user(create_user,driver_init,client):
    user = create_user(email='foo@bar.com', password='bar')
    assert user.is_authenticated is True  # <-- this should be False but it's True
    #assert user.is_anonymous is True      # <-- this fails
    #print("User=")
    #print("Full Name=" + str(client.login))
    #assert False
    client.login(email='foo@bar.com',password='bar')
    driver = driver_init
    nav_bar = NavBar(driver)
    login_page = LoginPage(driver)
    nav_bar.click_on_login()
    login_page.type_in_email('foo@bar.com')
    login_page.type_in_password('bar')
    login_page.click_on_login()
    time.sleep(100)


