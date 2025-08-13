import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class ElementActions:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Find element: {locator}. Waiting time: {timeout}')
    def find_element(self, locator, timeout=5):
        """Функція для очікування наявності елемента на сторінці"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise NoSuchElementException(f"Element {locator} not found for {timeout} second")

    @allure.step('Entering a value: {text} in an input field: {locator}')
    def fill_input(self, locator, text):
        """Функція для заповнення поля вводу текстом"""
        input_field = self.find_element(locator)
        input_field.clear()
        input_field.send_keys(text)

    @allure.step('Click button: {locator}')
    def click_button(self, locator):
        """Функція для очікування наявності та натискання кнопки"""
        button = self.find_element(locator)
        try:
            button.click()
        except Exception as e:
            print(f"Cannot click on button {locator}: {e}")

    @allure.step('Get text from locator: {locator}. Waiting time: {timeout}')
    def get_text(self, locator, timeout=5):
        """Функція отримання тексту з локатора"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.text
        except TimeoutException:
            raise NoSuchElementException(f"Element not found or not visible in {timeout} seconds")

    @allure.step('Checking the clickability of a button: {locator}. Waiting time: {timeout}')
    def button_is_clickable(self, locator, timeout=1):
        """Функція перевірки клікабельності кнопки"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutException:
            return False
