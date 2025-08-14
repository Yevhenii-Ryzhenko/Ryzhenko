import pytest
import allure

from lesson_28.conftest import driver, actions
from lesson_28.pages.sign_in_window import SignInWindow
from lesson_28.creds import CrateRandomData
from lesson_28.pages.locators import SignInWindowLocators

data = CrateRandomData
error_massage_to_qa_about_text_validation = "You did not receive the expected error"
error_massage_to_qa_about_button = 'Button "Register" is clickable, but you have invalid data'

@allure.epic('Validation')
@allure.feature('Registration')
@allure.feature('Authorization')
@pytest.mark.ui_tests
@pytest.mark.registration
@pytest.mark.authorization
@pytest.mark.testing_jenkins
class TestLogInWithoutPassword:

    @allure.story('Without password')
    def test_login_user_without_password(self, driver, url, home_page, actions):
        sign_in = SignInWindow(driver, url, home_page)
        sign_in.enter_one_data(locator=SignInWindowLocators.email_input_locator, value=data.email)
        actions.click_button(SignInWindowLocators.password_input_locator)
        actions.click_button(SignInWindowLocators.email_input_locator)
        error_text = actions.find_element(SignInWindowLocators.text_error_invalid_data_locator)
        assert "Password required" in error_text.text, error_massage_to_qa_about_text_validation
        assert actions.button_is_clickable(
            locator=SignInWindowLocators.button_login) is False, error_massage_to_qa_about_button