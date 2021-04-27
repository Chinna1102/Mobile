import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

class Mobile:
    def test(self):
        des_cap = {
            "deviceName": "Galaxy On Max",
            "platformName": "Android",
            "platformVersion": "8",
            "appPackage": "in.amazon.mShop.android.shopping",
            "appActivity": "com.amazon.mShop.home.HomeActivity"
            }
        url = "http://localhost:4723/wd/hub"
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=des_cap)
        time.sleep(5)
        cont=self.driver.find_element(By.ID, "sso_continue")
        cont.click()
        time.sleep(3)
        self.scrool_till_locator()
        self.get_locator()[0].click()

    def scroll_down(self):
        size=self.driver.get_window_size().get('height')
        start=int(size * 0.5)
        end=int(size * 0.2)
        tc = TouchAction(self.driver)

        tc.press(x=0,y=start).wait(2000).move_to(x=0,y=end).release().perform()
    def get_locator(self):
        see_more=self.driver.find_elements(By.XPATH, "//android.view.View[@content-desc='Explore more']")
        return  see_more
    def scrool_till_locator(self):
        while len(self.get_locator()) == 0:
            self.scroll_down()
m=Mobile()
m.test()