import allure

from lesson_28.actions import ElementActions
from lesson_28.pages.locators import AuthUserPageLocators, HomePageLocators

class AuthUserPage:

    def __init__(self, driver, url):
        self.url = url
        self.driver = driver
        self.actions = ElementActions(driver)

    @allure.step('Logout authorization user')
    def logout_auth_user(self):
        self.actions.click_button(AuthUserPageLocators.profile_button_locator)
        self.actions.click_button(AuthUserPageLocators.log_out_button)
        self.actions.find_element(HomePageLocators.header)