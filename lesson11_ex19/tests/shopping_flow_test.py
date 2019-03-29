from selenium import webdriver
import unittest
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

class ShoppingFlowTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.cart = CartPage(cls.driver)
        cls.product = ProductPage(cls.driver)
        cls.main = MainPage(cls.driver)
        cls.driver.maximize_window()

    def test_cart(self):
        product_name = ["Purple Duck", "Green Duck", "Blue Duck"]
        for product in product_name:
            self.main.open()        
            self.main.find_product(product)
            self.product.adding_to_cart("1")
        self.cart.checkout()
        self.cart.remove_items()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
