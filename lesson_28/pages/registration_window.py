from lesson_28.actions import ElementActions
from lesson_28.pages.locators import RegistrationWindowLocators, AuthUserPageLocators
from lesson_28.pages.home_page import HomePage

class RegistrationWindow:

    def __init__(self, driver, url, home_page: HomePage):
        self.url = url
        self.driver = driver
        self.actions = ElementActions(driver)
        self.home_page = home_page

    def open_registration_window(self):
        self.home_page.open_registration_window()
        self.actions.find_element(RegistrationWindowLocators.registration_text_locator)
        return self

    def enter_all_data(self, name:str, last_name:str, email: str, password: str, repeat_password:str):
        self.open_registration_window()
        assert self.actions.button_is_clickable(locator=RegistrationWindowLocators.button_register) is False
        self.actions.fill_input(RegistrationWindowLocators.name_input_locator, name)
        assert self.actions.button_is_clickable(locator=RegistrationWindowLocators.button_register) is False
        self.actions.fill_input(RegistrationWindowLocators.last_name_input_locator, last_name)
        assert self.actions.button_is_clickable(locator=RegistrationWindowLocators.button_register) is False
        self.actions.fill_input(RegistrationWindowLocators.email_input_locator, email)
        assert self.actions.button_is_clickable(locator=RegistrationWindowLocators.button_register) is False
        self.actions.fill_input(RegistrationWindowLocators.password_input_locator, password)
        assert self.actions.button_is_clickable(locator=RegistrationWindowLocators.button_register) is False
        self.actions.fill_input(RegistrationWindowLocators.repeat_password_input_locator, repeat_password)

    def register_with_existing_data(self, name:str, last_name:str, email: str, password: str, repeat_password:str):
        self.enter_all_data(name, last_name, email, password, repeat_password)
        self.actions.click_button(RegistrationWindowLocators.button_register)
        self.actions.find_element(AuthUserPageLocators.profile_button_locator)

    def enter_one_data(self, locator, text):
        self.actions.fill_input(locator, text)

