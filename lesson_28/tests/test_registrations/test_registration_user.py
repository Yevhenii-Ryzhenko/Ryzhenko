import pytest
import allure

from lesson_28.conftest import driver, actions
from lesson_28.pages.registration_window import RegistrationWindow
from lesson_28.creds import CrateRandomData
from lesson_28.pages.locators import AuthUserPageLocators, RegistrationWindowLocators

data = CrateRandomData

@allure.epic('Registration user')
@allure.feature('Registration')
@pytest.mark.ui_tests
@pytest.mark.registration
class TestRegistration:

    @pytest.mark.testing_jenkins
    @allure.story('Create new user')
    def test_create_new_user(self, driver, home_page, actions, url):
        register = RegistrationWindow(driver, url, home_page)
        register.register_with_existing_data(name=data.name, last_name=data.last_name,
                                             email=data.email, password=data.password, repeat_password=data.repeat_password)
        profile_button_text = actions.get_text(AuthUserPageLocators.profile_button_locator)
        assert profile_button_text == "My profile", "You not register new user"

    @allure.story('Checking the clickability of the "Register" button while gradually filling in the input fields')
    def test_button_unclickability(self, driver, home_page, actions, url):
        register = RegistrationWindow(driver, url, home_page)
        register.open_registration_window()
        error_msg_to_qa = 'Button "Register" is clickable, but you have not filled in all required fields'
        register.enter_one_data(RegistrationWindowLocators.name_input_locator, data.name)

        assert actions.button_is_clickable(locator=RegistrationWindowLocators.button_register) is False, error_msg_to_qa
        register.enter_one_data(RegistrationWindowLocators.last_name_input_locator, data.last_name)

        assert actions.button_is_clickable(locator=RegistrationWindowLocators.button_register) is False, error_msg_to_qa
        register.enter_one_data(RegistrationWindowLocators.email_input_locator, data.email)

        assert actions.button_is_clickable(locator=RegistrationWindowLocators.button_register) is False, error_msg_to_qa
        register.enter_one_data(RegistrationWindowLocators.password_input_locator, data.password)

        assert actions.button_is_clickable(locator=RegistrationWindowLocators.button_register) is False, error_msg_to_qa
        register.enter_one_data(RegistrationWindowLocators.repeat_password_input_locator, data.repeat_password)

        assert actions.button_is_clickable(locator=RegistrationWindowLocators.button_register), \
            "You have filled in all the fields, but the button is still not active"
