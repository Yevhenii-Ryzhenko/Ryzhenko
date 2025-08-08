import pytest

from lesson_28.conftest import driver, actions
from lesson_28.pages.sign_in_window import SignInWindow
from lesson_28.creds import CrateRandomData
from lesson_28.pages.locators import SignInWindowLocators

data = CrateRandomData
error_massage_to_qa_about_text_validation = "You did not receive the expected error"
error_massage_to_qa_about_button = 'Button "Register" is clickable, but you have invalid data'

def test_login_user_with_email_without_at(driver, url, home_page, actions):
    sign_in = SignInWindow(driver, url, home_page)
    sign_in.enter_data(email="example.email",
                                         password=data.password)
    error_text = actions.find_element(SignInWindowLocators.text_error_invalid_data_locator)
    assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=SignInWindowLocators.button_login) is False, error_massage_to_qa_about_button

def test_login_user_with_email_without_dot(driver, url, home_page, actions):
    sign_in = SignInWindow(driver, url, home_page)
    sign_in.enter_data(email="example@email",
                                         password=data.password)
    error_text = actions.find_element(SignInWindowLocators.text_error_invalid_data_locator)
    assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=SignInWindowLocators.button_login) is False, error_massage_to_qa_about_button

@pytest.mark.xfail(reason='Additional email validation checks will be added in future releases')
@pytest.mark.parametrize("character", ["&", "=", "+", "'"])
def test_login_user_with_email_start_prohibited_characters(driver, url, home_page, actions, character):
    sign_in = SignInWindow(driver, url, home_page)
    sign_in.enter_data(email=f"{character}email@example.com",
                                         password=data.password)
    error_text = actions.find_element(SignInWindowLocators.text_error_invalid_data_locator)
    assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=SignInWindowLocators.button_login) is False, error_massage_to_qa_about_button

@pytest.mark.parametrize("character", ["<", ">", ",", "."])
def test_login_user_with_email_starts_prohibited_characters(driver, url, home_page, actions, character):
    sign_in = SignInWindow(driver, url, home_page)
    sign_in.enter_data(email=f"{character}email@example.com",
                                         password=data.password)
    error_text = actions.find_element(SignInWindowLocators.text_error_invalid_data_locator)
    assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=SignInWindowLocators.button_login) is False, error_massage_to_qa_about_button

def test_login_user_with_email_start_space(driver, url, home_page, actions):
    sign_in = SignInWindow(driver, url, home_page)
    sign_in.enter_data(email=f" {data.email}",
                                         password=data.password)
    error_text = actions.find_element(SignInWindowLocators.text_error_invalid_data_locator)
    assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=SignInWindowLocators.button_login) is False, error_massage_to_qa_about_button

def test_login_user_with_email_ending_space(driver, url, home_page, actions):
    sign_in = SignInWindow(driver, url, home_page)
    sign_in.enter_data(email=f"{data.email} ",
                                         password=data.password)
    error_text = actions.find_element(SignInWindowLocators.text_error_invalid_data_locator)
    assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=SignInWindowLocators.button_login) is False, error_massage_to_qa_about_button

def test_login_user_with_email_with_space_in_middle(driver, url, home_page, actions):
    sign_in = SignInWindow(driver, url, home_page)
    sign_in.enter_data(email="example @email.com",
                                         password=data.password)
    error_text = actions.find_element(SignInWindowLocators.text_error_invalid_data_locator)
    assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
    assert actions.button_is_clickable(
        locator=SignInWindowLocators.button_login) is False, error_massage_to_qa_about_button



