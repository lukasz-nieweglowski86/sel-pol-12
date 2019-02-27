import unittest
from selenium import webdriver

class TestLitecartLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://localhost/litecart/admin/login.php")

    def test_login_page_elements_check(self):
        self.driver.find_element_by_xpath("//img[@alt='My Store']").click()
        self.driver.back()
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("admin")
        self.driver.find_element_by_name("remember_me").click()
        self.driver.find_element_by_name("login").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
