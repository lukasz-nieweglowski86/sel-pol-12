import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestLitecartMainPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://localhost/litecart/en/")

    def test_waits(self):
        product_name = ["Purple Duck", "Green Duck", "Blue Duck"]
        for product in product_name:
            self.driver.find_element_by_name("query").send_keys(product, Keys.RETURN)
            time.sleep(1)            
            self.driver.find_element_by_name("quantity").clear()
            self.driver.find_element_by_name("quantity").send_keys("2")
            self.driver.find_element_by_name("add_cart_product").click()
            print("%s added to cart." % product)
            time.sleep(1)
            self.driver.find_element_by_xpath("//i[@class='fa fa-home']").click()
            time.sleep(1)            
        self.driver.find_element_by_xpath("//a[text()='Checkout »']").click()
        time.sleep(1)
        products_in_cart = self.driver.find_elements_by_xpath("//ul[@class='shortcuts']")
        for product in products_in_cart:
            products_in_cart[0].click()
            time.sleep(1)
            self.driver.find_element_by_name("remove_cart_item").click()
            time.sleep(2)
            print("Item removed.")
            self.driver.refresh()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

if __name__ == '__main__':
    unittest.main()