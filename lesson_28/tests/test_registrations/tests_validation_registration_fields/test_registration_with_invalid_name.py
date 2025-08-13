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
class TestValidationNameInput:

    @allure.story('Length of name|last name')
    def test_create_user_with_name_less_2_characters(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name="Y",
                                last_name=data.last_name, email=data.email,
                                password=data.password, repeat_password=data.password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Name has to be from" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Length of name|last name')
    def test_create_user_with_name_more_20_characters(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name="ABCDEFGHIJKLMNOPQRSTU",
                                last_name=data.last_name, email=data.email,
                                password=data.password, repeat_password=data.password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Name has to be from" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Name|last name with integer|character')
    def test_create_user_with_name_with_int(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=f"{data.name}1",
                                last_name=data.last_name, email=data.email,
                                password=data.password, repeat_password=data.password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Name is invalid" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Name|last name with integer|character')
    def test_create_user_with_name_with_special_character(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=f"{data.name}!",
                                last_name=data.last_name, email=data.email,
                                password=data.password, repeat_password=data.password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Name is invalid" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Length of name|last name')
    def test_create_user_with_last_name_less_2_characters(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=data.name,
                                last_name="R",
                                email=data.email, password=data.password, repeat_password=data.password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Last name has to be from" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Length of name|last name')
    @pytest.mark.xfail(reason='Incorrect error text. The value "20" should be corrected to "30" in the next deployment')
    def test_create_user_with_last_name_more_20_characters(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=data.name,
                                last_name="ABCDEFGHIJKLMNOPQRSTUV",
                                email=data.email, password=data.password, repeat_password=data.password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Last name has to be from" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Length of name|last name')
    def test_create_user_with_last_name_more_30_characters(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=data.name,
                                last_name="ABCDEFGHIJKLMNOPQRSTUVWXYZYXWV",
                                email=data.email, password=data.password, repeat_password=data.password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Last name has to be from" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Name|last name with integer|character')
    def test_create_user_with_last_name_with_int(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=data.name,
                                last_name=f"{data.last_name}1",
                                email=data.email,
                                password=data.password, repeat_password=data.password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Last name is invalid" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button

    @allure.story('Name|last name with integer|character')
    def test_create_user_with_last_name_with_special_character(self, driver, url, home_page, actions):
        register = RegistrationWindow(driver, url, home_page)
        register.enter_all_data(name=data.name,
                                last_name=f"{data.last_name}!",
                                email=data.email,
                                password=data.password, repeat_password=data.password)
        error_text = actions.find_element(RegistrationWindowLocators.text_error_invalid_data_locator)
        assert "Last name is invalid" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=RegistrationWindowLocators.button_register) is False, error_massage_to_qa_about_button
