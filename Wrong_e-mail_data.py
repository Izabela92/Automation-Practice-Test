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

# TEST DATA
email = "adresemailpom.pl"
email2 = "adresemail@!!!.pl"
email3 = "aDresEmail+*@.pl"


class AutomationPracticeRegistration(unittest.TestCase):
    def setUp(self):
        # Preparation
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def testNoName(self):
        driver = self.driver


        sign_in_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
        sign_in_link.click()

        # 2. Type an e-mail adress
        email_input = driver.find_element(By.ID, "email_create")
        email_input.send_keys(email)

        # 3. Push the bottom „Create account”
        driver.find_element(By.NAME, "SubmitCreate").click()


        ## EXPECTED RESULT ##
        number_of_errors_text = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]/p').text
        self.assertEqual("There is 1 error", number_of_errors_text)
        error_messages_lwe = driver.find_elements(By.XPATH, '//div[@class="alert alert-danger"]/ol/li')

        self.assertEqual(1, len(error_messages_lwe))

        self.assertEqual("invalid e-mail adress.", error_messages_lwe[0].text)


        sleep(3)

    def testNoName2(self):
        driver = self.driver

        sign_in_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
        sign_in_link.click()

        # 2. Type an e-mail adress
        email_input = driver.find_element(By.ID, "email_create")
        email_input.send_keys(email2)

        # 3. Push the bottom „Create account”
        driver.find_element(By.NAME, "SubmitCreate").click()

        ## EXPECTED RESULT ##
        number_of_errors_text = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]/p').text
        self.assertEqual("There is 1 error", number_of_errors_text)
        error_messages_lwe = driver.find_elements(By.XPATH, '//div[@class="alert alert-danger"]/ol/li')

        self.assertEqual(1, len(error_messages_lwe))

        self.assertEqual("invalid e-mail adress.", error_messages_lwe[0].text)

        sleep(3)

    def testNoName3(self):
        driver = self.driver

        sign_in_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
        sign_in_link.click()

        # 2. Type an e-mail adress
        email_input = driver.find_element(By.ID, "email_create")
        email_input.send_keys(email3)

        # 3. Push the bottom „Create account”
        driver.find_element(By.NAME, "SubmitCreate").click()

        ## EXPECTED RESULT ##
        number_of_errors_text = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]/p').text
        self.assertEqual("There is 1 error", number_of_errors_text)
        error_messages_lwe = driver.find_elements(By.XPATH, '//div[@class="alert alert-danger"]/ol/li')

        self.assertEqual(1, len(error_messages_lwe))

        self.assertEqual("invalid e-mail adress.", error_messages_lwe[0].text)

        sleep(3)

    def tearDown(self):

        self.driver.quit()





