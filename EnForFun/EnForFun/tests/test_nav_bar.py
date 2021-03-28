import sys
import pytest

sys.path.append("..")
from pageObjects.NavBar import NavBar
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

def test_nav_bar_home(driver_init):
    driver = driver_init
    nav_bar = NavBar(driver)

    nav_bar.click_on_tutorials()
    nav_bar.check_tutorials_loaded()

    nav_bar.click_on_topics()
    nav_bar.check_topic_loaded("past-perfect")

    #nav_bar.click_on_home()
    #nav_bar.check_home_loaded()
    time.sleep(5)

