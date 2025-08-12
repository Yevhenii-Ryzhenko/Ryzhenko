from selenium.webdriver.common.by import By

class HomePageLocators:

    sign_in_button_locator = (By.XPATH, '//button[@class="btn btn-outline-white header_signin"]')
    header = (By.XPATH, '//div[@class="header_left d-flex align-items-center"]')

class SignInWindowLocators:

    log_in_text_locator = (By.XPATH, '//div[@class="modal-header"]//h4')
    email_input_locator = (By.ID, 'signinEmail')
    password_input_locator = (By.ID, 'signinPassword')
    button_login = (By.XPATH, '//div[@class="modal-footer d-flex justify-content-between"]//button[@class="btn btn-primary"]')
    button_registration = (By.XPATH, '//div[@class="modal-footer d-flex justify-content-between"]//button[@class="btn btn-link"]')
    error_registration_for_invalid_data = (By.XPATH, '//p[@class="alert alert-danger"]')
    text_error_invalid_data_locator = (By.XPATH, '//div[@class="invalid-feedback"]//p')

class RegistrationWindowLocators:

    registration_text_locator = (By.XPATH, '//div[@class="modal-header"]//h4')
    name_input_locator = (By.ID, 'signupName')
    last_name_input_locator = (By.ID, 'signupLastName')
    email_input_locator = (By.ID, 'signupEmail')
    password_input_locator = (By.ID, 'signupPassword')
    repeat_password_input_locator = (By.ID, 'signupRepeatPassword')
    button_register = (By.XPATH, '//div[@class="modal-footer"]//button[@class="btn btn-primary"]')
    text_error_invalid_data_locator = (By.XPATH, '//div[@class="invalid-feedback"]//p')

class AuthUserPageLocators:

    profile_button_locator = (By.ID, 'userNavDropdown')
    log_out_button = (By.XPATH, '//button[@class="dropdown-item btn btn-link user-nav_link"]')



