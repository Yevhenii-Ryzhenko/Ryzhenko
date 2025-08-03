from selenium.webdriver.common.by import By

class TrackingPageLocators:

    parcel_number_input_loc = (By.XPATH, '//input[@class="track__form-group-input"]')
    search_button_loc = (By.ID, 'np-number-input-desktop-btn-search-en')
    status_parcel_loc = (By.XPATH, '//div[@class="header__status-text"]')
    massager_window = (By.XPATH, '//div[@class="conversation"]')
    error_massage = (By.XPATH, '//div[@id="np-number-input-desktop-message-error-message"]//span')