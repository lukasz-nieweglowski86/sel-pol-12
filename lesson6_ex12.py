import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import os

class TestLitecartAdminPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://localhost/litecart/admin/login.php")
        cls.driver.find_element_by_name("username").send_keys("admin")
        cls.driver.find_element_by_name("password").send_keys("admin")
        cls.driver.find_element_by_name("remember_me").click()
        cls.driver.find_element_by_name("login").click()

    def test_adding_product(self):
        self.driver.find_element_by_xpath("//span[text()='Catalog']").click()
        self.driver.find_element_by_xpath("//a[text()=' Add New Product']").click()
        self.driver.find_element_by_xpath("//input[@type='radio' and @value='1']").click()
        self.driver.find_element_by_name("name[en]").send_keys("Pink Duck")
        self.driver.find_element_by_name("code").send_keys("rd006")
        self.driver.find_element_by_xpath("//input[@data-name='Rubber Ducks']").click()
        select = Select(self.driver.find_element_by_name("default_category_id"))
        select.select_by_value("1")
        self.driver.find_element_by_xpath("//input[@value='1-3' and @type='checkbox']").click()
        self.driver.find_element_by_name("quantity").send_keys("1000")
        path = os.path.abspath('.\\pink_duck.jpg')
        self.driver.find_element_by_name("new_images[]").clear()
        self.driver.find_element_by_name("new_images[]").send_keys(path)
        self.driver.find_element_by_name("date_valid_from").send_keys("2018-01-01")
        self.driver.find_element_by_name("date_valid_to").send_keys("2020-01-01")
        





    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

if __name__ == '__main__':
    unittest.main()