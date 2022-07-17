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

# DANE TESTOWE
email = "adresemail@pom.pl"
sex = "F"
last_name = "Kowalska"
password = "ddjh2!jfD"
birthdate = "27-08-1992"
address = "ul. Zamenhofa 120"
city = "Poznan"
postal_code = "16473"
phone_mobile = "605-732-869"
state = "Florida"
alias = "moj domowy adres"

class AutomationPracticeRegistration(unittest.TestCase):
    def setUp(self):
        # Przygotowanie testu
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def testNoName(self):
        driver = self.driver

        # Kroki
        # 1. Kliknij „Sign in”
        # a) Znaleźć ten element na stronie przy pomocy inspektora
        # b) Dobrać odpowiedni lokator w Selenium
        # c) Przy pomocy drivera zlokalizować ten element
        # (mam ten element)
        # sign_in_link = driver.find_element_by_partial_link_text("Sign in")

        sign_in_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
        sign_in_link.click()

        # 2. Wpisz e-mail
        email_input = driver.find_element(By.ID, "email_create")
        email_input.send_keys(email)

        # 3. Kliknij przycisk „Create account”
        driver.find_element(By.NAME, "SubmitCreate").click()

        # 4. Wybierz płeć
        if sex == "F":
            # wybierz Mrs
            driver.find_element(By.ID, "id_gender2").click()

        else:
            # Wybierz Mr
            driver.find_element(By.ID, "id_gender1").click()

        # 5. Wpisz nazwisko
        driver.find_element(By.CSS_SELECTOR, 'input[id="customer_lastname"]').send_keys(last_name)

        # 6. Sprawdź poprawność e-maila
        personal_info_email_input = driver.find_element(By.XPATH, '//input[@id="email"]')
        email_fact = personal_info_email_input.get_attribute("value")
        self.assertEqual(email, email_fact)

        # 7. Wpisz hasło
        driver.find_element(By.ID, "passwd").send_keys(password)

        # 8. Wybierz datę urodzenia
        birthdate_l = birthdate.split("-")
        days_s = Select(driver.find_element(By.ID, "days"))
        days_s.select_by_value(str(int(birthdate_l[0])))
        months_s = Select(driver.find_element(By.ID, "months"))
        months_s.select_by_value(str(int(birthdate_l[1])))
        year_s = Select(driver.find_element(By.ID, "years"))
        year_s.select_by_value(str(int(birthdate_l[2])))

        # 9. Sprawdź pole „First name”
        first_name_fact = driver.find_element(By.ID, "firstname").get_attribute("value")
        self.assertEqual("", first_name_fact)

        # 10. Sprawdź pole „Last name”
        last_name_fact = driver.find_element(By.ID, "lastname").get_attribute("value")
        self.assertEqual(last_name, last_name_fact)

        # 11. Wpisz adres
        address_input = driver.find_element(By.ID, "address1")
        address_input.send_keys(address)

        # 12. Wpisz miasto
        city_input = driver.find_element(By.NAME, 'city')
        city_input.send_keys(city)

        # 13. Wpisz kod pocztowy
        driver.find_element(By.ID, 'postcode').send_keys(postal_code)
        state_s = Select(driver.find_element(By.ID, 'id_country'))
        state_s.select_by_value("21")

        # 14.Wybierz stan
        state_s = Select(driver.find_element(By.ID, 'id_state'))
        state_s.select_by_value("9")

        # 15.Wpisz nr telefonu komórkowego
        driver.find_element(By.NAME, 'phone_mobile')
        phone_mobile_input.send_keys(phone_mobile)

        # 16.Wpisz alias adresu
        empty_alias = driver.find_element(By.ID, 'alias')
        empty_alias.clear()
        empty_alias.send_keys("Jaki alias")

        # 17.Kliknij Register
        driver.find_element(By.ID, 'submitAccount').click()

        ## OCZEKIWANY REZULTAT ##
        number_of_errors_text = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]/p').text
        self.assertEqual("There is 1 error", number_of_errors_text)
        error_messages_lwe = driver.find_elements(By.XPATH, '//div[@class="alert alert-danger"]/ol/li')
        # Sprawdzam, czy wyświetlony jest tylko jeden komunikat o błędzie
        self.assertEqual(1, len(error_messages_lwe))
        # Sprawdzam treść tego komunikatu
        self.assertEqual("firstname is required.", error_messages_lwe[0].text)


        sleep(3)



    def tearDown(self):
        # Zakończenie testu
        self.driver.quit()


