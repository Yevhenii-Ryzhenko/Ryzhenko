import allure

from lesson_28.actions import ElementActions
from lesson_28.pages.locators import HomePageLocators, SignInWindowLocators

class HomePage:

    def __init__(self, driver, url):
        self.url = url
        self.driver = driver
        self.actions = ElementActions(driver)

    @allure.step('Open home page')
    def open_page(self):
        self.driver.get(self.url)
        self.actions.find_element(HomePageLocators.header)
        return self

    @allure.step('Open home page -> Open LogIn window')
    def open_sign_in_window(self):
        self.open_page()
        self.actions.click_button(HomePageLocators.sign_in_button_locator)
        return self

    @allure.step('Open home page -> Open LogIn window -> Open registration window')
    def open_registration_window(self):
        self.open_sign_in_window()
        self.actions.click_button(SignInWindowLocators.button_registration)
        return self


