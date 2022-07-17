from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
from time import sleep

class AutomationPracticeBasket(unittest.TestCase):
    def setUp(self):
        # Przygotowanie testu
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def testNoName(self):
        driver = self.driver

        add_to_cart = driver.find_element(By.CSS_SELECTOR, "homefeatured > li:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > a:nth-child(1)")
        add_to_cart.click()

        print(add_to_cart)
        sleep(3)

    def tearDown(self):
        self.driver.quit()