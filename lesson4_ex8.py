import unittest
from selenium import webdriver

class TestLitecartMainPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://localhost/litecart/en/")

    def test_count_stickers(self):
        product_list = self.driver.find_elements_by_xpath("//li[contains(@class,'product')]")
        for product in product_list:
            sticker_count = len(product.find_elements_by_xpath("a/div/div[contains(@class,'sticker')]"))
            if sticker_count == 1:
                print("Product has only 1 sticker.")
            else:
                print("Product does not have only 1 sticker.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()