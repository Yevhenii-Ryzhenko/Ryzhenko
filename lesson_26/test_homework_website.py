# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pytest
#
# driver = webdriver.Chrome()
# driver.get("http://localhost:8000/dz.html")
#
# class TestFrame1:
#
#     def switch_to_frame_1(self):
#         driver.switch_to.default_content()
#         driver.switch_to.frame(driver.find_element(By.ID, "frame1"))
#
#     def test_frame_1_text(self):
#         self.switch_to_frame_1()
#
#         frame1_text = driver.find_element(By.XPATH, "//body/h3")
#         assert frame1_text.text == "Frame1"
#
#     def test_frame_1_input_text(self):
#         self.switch_to_frame_1()
#
#         input_text = driver.find_element(By.ID, "input1")
#         assert input_text.get_attribute("placeholder") == "Введіть текст"
#
#     def test_frame_1_button_text(self):
#         self.switch_to_frame_1()
#
#         button_text = driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input1')\"]")
#         assert button_text.text == "Перевірити"
#
#     def test_frame1_secret(self):
#         self.switch_to_frame_1()
#
#         frame1_secret = driver.find_element(By.ID, "input1")
#         frame1_secret.send_keys("Слава Україні!")
#         check_button = driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input1')\"]")
#         check_button.click()
#         alert = driver.switch_to.alert
#         assert alert.text == "Героям Слава!", "Incorrect alert text"
#         alert.accept()
#         frame1_secret.clear()
#
#     def test_frame1_secret_negative(self):
#         self.switch_to_frame_1()
#
#         frame1_secret = driver.find_element(By.ID, "input1")
#         frame1_secret.send_keys("Слава україні!")
#         check_button = driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input1')\"]")
#         check_button.click()
#         alert = driver.switch_to.alert
#         assert alert.text == "Геть звідси, розбійнику!", "Incorrect alert text"
#         alert.accept()
#         frame1_secret.clear()
#
#     def test_frame1_empty_input(self):
#         self.switch_to_frame_1()
#
#         check_button = driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input1')\"]")
#         check_button.click()
#         alert = driver.switch_to.alert
#         assert alert.text == "Геть звідси, розбійнику!", "Incorrect alert text"
#         alert.accept()
#
#
# class TestTestFrame2:
#
#     def switch_to_frame_2(self):
#         driver.switch_to.default_content()
#         driver.switch_to.frame(driver.find_element(By.ID, "frame2"))
#
#     def test_frame_2_text(self):
#         self.switch_to_frame_2()
#
#         frame2_text = driver.find_element(By.XPATH, "//body/h3")
#         assert frame2_text.text == "Frame2"
#
#     def test_frame_2_input_text(self):
#         self.switch_to_frame_2()
#
#         input_text = driver.find_element(By.ID, "input2")
#         assert input_text.get_attribute("placeholder") == "Введіть текст"
#
#     def test_frame_1_button_text(self):
#         self.switch_to_frame_2()
#
#         button_text = driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input2')\"]")
#         assert button_text.text == "Перевірити"
#
#
#     def test_frame2_secret(self):
#         self.switch_to_frame_2()
#
#         frame2_secret = driver.find_element(By.ID, "input2")
#         frame2_secret.send_keys("Слава Нації!")
#         check_button = driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input2')\"]")
#         check_button.click()
#         alert = driver.switch_to.alert
#         assert alert.text == "Смерть ворогам!", "Incorrect alert text"
#         alert.accept()
#         frame2_secret.clear()
#
#     def test_frame2_secret_negative(self):
#         self.switch_to_frame_2()
#
#         frame2_secret = driver.find_element(By.ID, "input2")
#         frame2_secret.send_keys("Слава нації!")
#         check_button = driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input2')\"]")
#         check_button.click()
#         alert = driver.switch_to.alert
#         assert alert.text == "Навіть не намагайся!", "Incorrect alert text"
#         alert.accept()
#         frame2_secret.clear()
#
#     def test_frame2_empty_input(self):
#         self.switch_to_frame_2()
#
#         check_button = driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input2')\"]")
#         check_button.click()
#         alert = driver.switch_to.alert
#         assert alert.text == "Навіть не намагайся!", "Incorrect alert text"
#         alert.accept()