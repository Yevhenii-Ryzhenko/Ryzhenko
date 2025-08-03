import pytest
import random
from lesson_27.np_tracking_page.locators import TrackingPageLocators

def test_random_parcel_number(tracking_page):
    tracking_page.open_page()
    assert tracking_page.actions.is_clickable(TrackingPageLocators.search_button_loc) is False
    parcel_number = f"2040046642{random.randint(1000,9999)}"
    tracking_page.fill_parcel_number(parcel_number)
    assert tracking_page.actions.is_clickable(TrackingPageLocators.search_button_loc) is True
    tracking_page.actions.click_button(locator=TrackingPageLocators.search_button_loc)
    tracking_page.actions.find_element(TrackingPageLocators.massager_window)

def test_real_parcel_number(tracking_page):
    tracking_page.open_page()
    assert tracking_page.actions.is_clickable(TrackingPageLocators.search_button_loc) is False
    parcel_number = 20400466426374
    tracking_page.fill_parcel_number(parcel_number)
    assert tracking_page.actions.is_clickable(TrackingPageLocators.search_button_loc) is True
    tracking_page.actions.click_button(locator=TrackingPageLocators.search_button_loc)
    text = tracking_page.actions.get_text(TrackingPageLocators.status_parcel_loc)
    assert text == "Отримана"

def test_parcel_number_negative(tracking_page):
    tracking_page.open_page()
    assert tracking_page.actions.is_clickable(TrackingPageLocators.search_button_loc) is False
    parcel_number = f"1234567890{random.randint(1000,9999)}"
    tracking_page.fill_parcel_number(parcel_number)
    assert tracking_page.actions.is_clickable(TrackingPageLocators.search_button_loc) is True
    tracking_page.actions.click_button(locator=TrackingPageLocators.search_button_loc)
    text = tracking_page.actions.get_text(TrackingPageLocators.error_massage)
    assert "Ми не знайшли посилку за таким номером" in text

def test_button_is_unclickable(tracking_page):
    tracking_page.open_page()
    assert tracking_page.actions.is_clickable(TrackingPageLocators.search_button_loc) is False
    parcel_number = f"{random.randint(1000,99999)}"
    tracking_page.fill_parcel_number(parcel_number)
    assert tracking_page.actions.is_clickable(TrackingPageLocators.search_button_loc) is False
