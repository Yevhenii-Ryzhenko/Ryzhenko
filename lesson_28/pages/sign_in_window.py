from lesson_28.actions import ElementActions
from lesson_28.pages.locators import SignInWindowLocators, AuthUserPageLocators
from lesson_28.pages.home_page import HomePage

class SignInWindow:

    def __init__(self, driver, url, home_page: HomePage):
        self.url = url
        self.driver = driver
        self.actions = ElementActions(driver)
        self.home_page = home_page

    def open_registration_window(self):
        self.home_page.open_sign_in_window()
        self.actions.find_element(SignInWindowLocators.log_in_text_locator)
        return self

    def enter_data(self, email: str, password: str):
        self.open_registration_window()
        assert self.actions.button_is_clickable(locator=SignInWindowLocators.button_login) is False
        self.actions.fill_input(SignInWindowLocators.email_input_locator, email)
        self.actions.fill_input(SignInWindowLocators.password_input_locator, password)

    def login_with_existing_data(self, email, password):
        self.enter_data(email=email, password=password)
        self.actions.click_button(SignInWindowLocators.button_login)
        self.actions.find_element(AuthUserPageLocators.profile_button_locator)

    def enter_one_data(self, locator, value):
        self.open_registration_window()
        assert self.actions.button_is_clickable(locator=SignInWindowLocators.button_login) is False
        self.actions.fill_input(locator, value)

