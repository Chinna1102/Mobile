import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

des_cap = {
    "deviceName": "Galaxy On Max",
    "platformName": "Android",
    "platformVersion": "8",
    "appPackage": "dragdrop.stufflex.com.dragdrop",
    "appActivity": "dragdrop.stufflex.com.dragdrop.splash"
}
url = "http://localhost:4723/wd/hub"

driver = webdriver.Remote(command_executor=url, desired_capabilities=des_cap)
time.sleep(5)

football = driver.find_element(By.ID, "btn_football")
football.click()

time.sleep(3)

SRC = driver.find_element(By.ID, "chooseC")
DES = driver.find_element(By.ID, "answer")

tc = TouchAction(driver)

tc.long_press(el=SRC).move_to(el=DES).release().perform()

time.sleep(3)

a=DES.text
print(a)
