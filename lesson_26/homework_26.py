from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000/dz.html")

time.sleep(2)

driver.switch_to.frame(driver.find_element(By.ID, "frame1"))

frame1_secret = driver.find_element(By.ID, "input1")
frame1_secret.send_keys("Слава Україні!")

time.sleep(3)

check_button = driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input1')\"]")
check_button.click()

time.sleep(3)

alert = driver.switch_to.alert
alert.accept()

driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.ID, "frame2"))

frame2_secret = driver.find_element(By.ID, "input2")
frame2_secret.send_keys("Слава Нації!")

time.sleep(3)

check_button = driver.find_element(By.XPATH, "//button[@onclick=\"verifyInput('input2')\"]")
check_button.click()

time.sleep(3)

alert = driver.switch_to.alert
alert.accept()

time.sleep(3)

driver.quit()