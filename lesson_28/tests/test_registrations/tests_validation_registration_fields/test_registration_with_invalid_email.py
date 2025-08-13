import pytest
import allure

from lesson_28.conftest import driver, actions
from lesson_28.pages.registration_window import RegistrationWindow
from lesson_28.creds import CrateRandomData
from lesson_28.pages.locators import RegistrationWindowLocators

data = CrateRandomData
error_massage_to_qa_about_text_validation = "You did not receive the expected error"
error_massage_to_qa_about_button = 'Button "Register" is clickable, but you have invalid data'


@allure.epic('Validation')
@allure.feature('Registration')
@pytest.mark.ui_tests
@pytest.mark.registration
class TestValidationEmailInput:

    @allure.story('Email with character')
    def test_create_user_with_email_without_at(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=data.name, last_name=data.last_name,
                                             email="example.email",
                                             password=data.password, repeat_password=data.repeat_password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Email with character')
    def test_create_user_with_email_without_dot(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=data.name, last_name=data.last_name,
                                             email="example@email",
                                             password=data.password, repeat_password=data.repeat_password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Email with character')
    @pytest.mark.xfail(reason='Additional email validation checks will be added in future releases')
    @pytest.mark.parametrize("character", ["&", "=", "+", "'"])
    def test_create_user_with_email_start_prohibited_characters(self, driver, url, home_page, actions, character):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=data.name, last_name=data.last_name,
                                             email=f"{character}email@example.com",
                                             password=data.password, repeat_password=data.repeat_password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Email with character')
    @pytest.mark.parametrize("character", ["<", ">", ",", "."])
    def test_create_user_with_email_starts_prohibited_characters(self, driver, url, home_page, actions, character):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=data.name, last_name=data.last_name,
                                             email=f"{character}email@example.com",
                                             password=data.password, repeat_password=data.repeat_password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Email with space')
    def test_create_user_with_email_start_space(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=data.name, last_name=data.last_name,
                                             email=f" {data.email}",
                                             password=data.password, repeat_password=data.repeat_password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Email with space')
    def test_create_user_with_email_ending_space(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=data.name, last_name=data.last_name,
                                             email=f"{data.email} ",
                                             password=data.password, repeat_password=data.repeat_password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Email with space')
    def test_create_user_with_email_with_space_in_middle(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=data.name, last_name=data.last_name,
                                             email="example @email.com",
                                             password=data.password, repeat_password=data.repeat_password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Email is incorrect" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

