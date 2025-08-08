import pytest
from selenium import webdriver
from lesson_28.pages.home_page import HomePage
from lesson_28.creds import Creds
from lesson_28.actions import ElementActions


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver, url=f"https://{Creds.login}:{Creds.password}@qauto2.forstudy.space")

@pytest.fixture
def actions(driver):
    return ElementActions(driver)

@pytest.fixture
def url(home_page):
    return home_page.url