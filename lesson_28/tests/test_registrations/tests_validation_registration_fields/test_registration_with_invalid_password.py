import pytest

from lesson_28.conftest import driver, actions
from lesson_28.pages.registration_window import RegistrationWindow
from lesson_28.creds import CrateRandomData
from lesson_28.pages.locators import RegistrationWindowLocators

data = CrateRandomData
error_massage_to_qa_about_text_validation = "You did not receive the expected error"
error_massage_to_qa_about_button = 'Button "Register" is clickable, but you have invalid data'


def test_create_user_with_invalid_password(driver, url, home_page, actions):
    register = RegistrationWindow(driver, url, home_page)
    register.enter_all_data(name=data.name, last_name=data.last_name,
                                         email=data.email,
                                         password="Test123", repeat_password="Test123")
    error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
    assert "Password has to be from" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

def test_create_user_with_different_password(driver, url, home_page, actions):
    register = RegistrationWindow(driver, url, home_page)
    register.enter_all_data(name=data.name, last_name=data.last_name,
                                         email=data.email,
                                         password="Test1234", repeat_password="Test1235")
    actions.click_button(RegistrationWindowLocators.email_input_locator)
    error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
    assert "Passwords do not match" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

def test_create_user_with_password_only_small_letters(driver, url, home_page, actions):
    register = RegistrationWindow(driver, url, home_page)
    register.enter_all_data(name=data.name, last_name=data.last_name,
                                         email=data.email,
                                         password="test1pass", repeat_password="test1pass")
    actions.click_button(RegistrationWindowLocators.email_input_locator)
    error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
    assert "Password has to be from" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

def test_create_user_with_password_only_capital_letters(driver, url, home_page, actions):
    register = RegistrationWindow(driver, url, home_page)
    register.enter_all_data(name=data.name, last_name=data.last_name,
                                         email=data.email,
                                         password="TEST1PASS", repeat_password="TEST1PASS")
    actions.click_button(RegistrationWindowLocators.email_input_locator)
    error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
    assert "Password has to be from" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

def test_create_user_with_password_only_integer(driver, url, home_page, actions):
    register = RegistrationWindow(driver, url, home_page)
    register.enter_all_data(name=data.name, last_name=data.last_name,
                                         email=data.email,
                                         password="1234567890", repeat_password="1234567890")
    actions.click_button(RegistrationWindowLocators.email_input_locator)
    error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
    assert "Password has to be from" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

def test_create_user_with_password_less_8_characters(driver, url, home_page, actions):
    register = RegistrationWindow(driver, url, home_page)
    register.enter_all_data(name=data.name, last_name=data.last_name,
                                         email=data.email,
                                         password="Test123", repeat_password="Test123")
    actions.click_button(RegistrationWindowLocators.email_input_locator)
    error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
    assert "Password has to be from" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

def test_create_user_with_password_more_15_characters(driver, url, home_page, actions):
    register = RegistrationWindow(driver, url, home_page)
    register.enter_all_data(name=data.name, last_name=data.last_name,
                                         email=data.email,
                                         password="Testpassword1234", repeat_password="Testpassword1234")
    actions.click_button(RegistrationWindowLocators.email_input_locator)
    error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
    assert "Password has to be from" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

