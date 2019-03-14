import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestLitecartMainPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://localhost/litecart/en/")

    def test_registration(self):
        self.driver.find_element_by_xpath("//a[text()='New customers click here']").click()

        self.driver.find_element_by_name("tax_id").send_keys("PLdddddddddd")

        self.driver.find_element_by_name("company").send_keys("Lukasz Nieweglowski Inc.")

        self.driver.find_element_by_name("firstname").send_keys("Lukasz")

        self.driver.find_element_by_name("lastname").send_keys("Nieweglowski")

        self.driver.find_element_by_name("address1").send_keys("Rapackiego")

        self.driver.find_element_by_name("address2").send_keys("123a")

        self.driver.find_element_by_name("postcode").send_keys("22-222")

        self.driver.find_element_by_name("city").send_keys("Lublin")

        self.driver.find_element_by_xpath("//span[@class='select2-selection__arrow']").click()        
        self.driver.find_element_by_xpath("//input[@class='select2-search__field']").send_keys("Poland", Keys.RETURN)

        # select = self.driver.find_element_by_xpath("//input[@name='zone_code']")
        # self.driver.execute_script("arguments[0].selectedIndex = 1;", select)

        self.driver.find_element_by_name("email").send_keys("lukasz.nieweglowski86+{}@gmail.com".format(time.time()))
        user_email = self.driver.find_element_by_name("email").get_attribute("value")

        self.driver.find_element_by_name("phone").send_keys("123123123")

        self.driver.find_element_by_xpath("//input[@name='newsletter']").click()

        user_password = "Qwerty123"
        self.driver.find_element_by_name("password").send_keys(user_password)
        self.driver.find_element_by_name("confirmed_password").send_keys(user_password)

        self.driver.find_element_by_xpath("//button[@name='create_account']").click()

        self.driver.find_element_by_xpath("//a[text()='Logout']").click()

        self.driver.find_element_by_name("email").send_keys(user_email)
        self.driver.find_element_by_name("password").send_keys(user_password)
        self.driver.find_element_by_xpath("//button[@name='login']").click()

        self.driver.find_element_by_xpath("//a[text()='Logout']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()