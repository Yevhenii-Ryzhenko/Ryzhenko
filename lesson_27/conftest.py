import pytest
from selenium import webdriver
from lesson_27.np_tracking_page.tracking_page import TrackingPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def tracking_page(driver):
    return TrackingPage(driver, url="https://tracking.novaposhta.ua/#/uk")