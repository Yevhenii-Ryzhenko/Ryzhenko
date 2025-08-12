import pytest

from lesson_28.conftest import driver, actions
from lesson_28.pages.registration_window import RegistrationWindow
from lesson_28.pages.auth_user_page import AuthUserPage
from lesson_28.pages.sign_in_window import SignInWindow
from lesson_28.creds import CrateRandomData
from lesson_28.pages.locators import AuthUserPageLocators


data = CrateRandomData

def test_registr_and_auth_new_user(driver, home_page, actions, url):
    register = RegistrationWindow(driver, url, home_page)
    register.register_with_existing_data(name=data.name, last_name=data.last_name,
                                         email=data.email, password=data.password, repeat_password=data.repeat_password)
    logout = AuthUserPage(driver, url)
    logout.logout_auth_user()
    sign_in = SignInWindow(driver, url, home_page)
    sign_in.login_with_existing_data(email=data.email, password=data.password)
    profile_button_text = actions.get_text(AuthUserPageLocators.profile_button_locator)
    assert profile_button_text == "My profile", "You not register new user"