import pytest
from selenium import webdriver
from lesson_28.pages.home_page import HomePage
from lesson_28.creds import Creds
from lesson_28.actions import ElementActions
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    print("Driver fixture used, headless mode on")
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    print("HomePage URL:", url)
    return HomePage(driver, url=f"https://{Creds.login}:{Creds.password}@qauto2.forstudy.space")

@pytest.fixture
def actions(driver):
    return ElementActions(driver)

@pytest.fixture
def url(home_page):
    return home_page.url