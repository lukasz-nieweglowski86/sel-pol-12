import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestLitecartMainPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://localhost/litecart/en/")

    def test_waits(self):
        wait = WebDriverWait(self.driver, 10)
        product_name = ["Purple Duck", "Green Duck", "Blue Duck"]
        for product in product_name:
            self.driver.find_element_by_name("query").send_keys(product, Keys.RETURN)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='title' and text()='%s']" % product)))
            self.driver.find_element_by_name("quantity").clear()
            self.driver.find_element_by_name("quantity").send_keys("2")
            amount_in_cart = self.driver.find_element_by_xpath("//span[@class='quantity']").get_attribute("textContent")
            self.driver.find_element_by_name("add_cart_product").click()
            print("%s added to cart." % product)
            wait.until_not(EC.text_to_be_present_in_element((By.XPATH, "//span[@class='quantity']"), amount_in_cart))
            self.driver.find_element_by_xpath("//i[@class='fa fa-home']").click()
        self.driver.find_element_by_xpath("//a[text()='Checkout »']").click()
        products_in_cart = len(self.driver.find_elements_by_xpath("//ul[@class='shortcuts']/li"))
        for i in range(0, products_in_cart):
            ducks_name = self.driver.find_element_by_xpath("//p[@style='margin-top: 0px;']/a/strong")            
            self.driver.find_element_by_name("remove_cart_item").click()
            wait.until(EC.staleness_of(ducks_name))
            print("Item removed.")
            
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()