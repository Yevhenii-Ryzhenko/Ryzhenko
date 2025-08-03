from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class ElementActions:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=5):
        """Функція для очікування наявності елемента на сторінці"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise NoSuchElementException(f"Element not found for {timeout} second")

    def fill_input(self, locator, text):
        """Функція для заповнення поля вводу текстом"""
        input_field = self.find_element(locator)
        input_field.clear()
        input_field.send_keys(text)

    def click_button(self, locator):
        """Функція для очікування наявності та натискання кнопки"""
        button = self.find_element(locator)
        button.click()

    def get_text(self, locator, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.text
        except TimeoutException:
            raise NoSuchElementException(f"Element not found or not visible in {timeout} seconds")

    def is_clickable(self, locator, timeout=1):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutException:
            return False
