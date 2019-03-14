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
        # opening Catalog
        self.driver.find_element_by_xpath("//span[text()='Catalog']").click() 

        # clicking on 'Add new product'
        self.driver.find_element_by_xpath("//a[text()=' Add New Product']").click() 

        # filling 'General' tab
        self.driver.find_element_by_xpath("//input[@type='radio' and @value='1']").click() 
        new_product_name = "Pink Duck"
        self.driver.find_element_by_name("name[en]").send_keys(new_product_name)
        self.driver.find_element_by_name("code").send_keys("rd006")
        self.driver.find_element_by_xpath("//input[@data-name='Rubber Ducks']").click()
        select = Select(self.driver.find_element_by_name("default_category_id"))
        select.select_by_value("1")
        self.driver.find_element_by_xpath("//input[@value='1-3' and @type='checkbox']").click()
        self.driver.find_element_by_name("quantity").send_keys("100")
        path = os.path.abspath('.\\pink_duck.jpg')
        self.driver.find_element_by_name("new_images[]").clear()
        self.driver.find_element_by_name("new_images[]").send_keys(path)
        self.driver.find_element_by_name("date_valid_from").send_keys("2018-01-01")
        self.driver.find_element_by_name("date_valid_to").send_keys("2020-01-01")
        
        # switching to 'Information' tab
        self.driver.find_element_by_xpath("//a[text()='Information']").click() 

        # filling 'Information' tab
        select = Select(self.driver.find_element_by_name("manufacturer_id")) 
        select.select_by_value("1")
        self.driver.find_element_by_name("keywords").send_keys(new_product_name)
        description_text = "Lorem ipsum... "
        self.driver.find_element_by_name("short_description[en]").send_keys(description_text)
        self.driver.find_element_by_xpath("//div[@class='trumbowyg-editor']").send_keys(description_text * 5)
        self.driver.find_element_by_name("head_title[en]").send_keys(new_product_name)
        self.driver.find_element_by_name("meta_description[en]").send_keys(new_product_name)

        # switching to 'Prices' tab
        self.driver.find_element_by_xpath("//a[text()='Prices']").click() 

        # filling 'Prices' tab
        self.driver.find_element_by_name("purchase_price").send_keys("21")  
        select = Select(self.driver.find_element_by_name("purchase_price_currency_code"))
        select.select_by_value("USD")
        self.driver.find_element_by_name("prices[USD]").send_keys("17")
        self.driver.find_element_by_name("gross_prices[USD]").send_keys("21")
        self.driver.find_element_by_name("prices[EUR]").send_keys("13")
        self.driver.find_element_by_name("gross_prices[EUR]").send_keys("16")

        # saving new product
        self.driver.find_element_by_name("save").click() 

        # checking if the new product has appeard in the Catalog
        print(self.driver.find_element_by_xpath("//tr[@class='row'][3]/td[3]").get_attribute("textContent") + " is present in the Catalog.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()