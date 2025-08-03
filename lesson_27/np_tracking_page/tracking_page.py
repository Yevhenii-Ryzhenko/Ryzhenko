from lesson_27.ui_utils.processing_element import ElementActions
from lesson_27.np_tracking_page.locators import TrackingPageLocators

class TrackingPage:

    def __init__(self, driver, url):
        self.url = url
        self.driver = driver
        self.actions = ElementActions(driver)

    def open_page(self):
        self.driver.get(self.url)
        return self

    def fill_parcel_number(self, number):
        self.actions.fill_input(TrackingPageLocators.parcel_number_input_loc, number)

    def click_search_button(self):
        self.actions.click_button(TrackingPageLocators.search_button_loc)

