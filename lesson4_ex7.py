import unittest
from selenium import webdriver

class TestLitecartLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://localhost/litecart/admin/login.php")
        cls.driver.find_element_by_name("username").send_keys("admin")
        cls.driver.find_element_by_name("password").send_keys("admin")
        cls.driver.find_element_by_name("remember_me").click()
        cls.driver.find_element_by_name("login").click()

    def test_appearence_category(self):
        self.driver.find_element_by_xpath("//span[text()='Appearence']").click()
        self.assertEquals(self.driver.find_element_by_xpath("//span[text()='Template']"), "")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()