import unittest
from selenium import webdriver

class TestLitecartMainPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://localhost/litecart/en/")

    def test_count_stickers(self):
        print(len(self.driver.find_elements_by_xpath("//div[contains(@class,'sticker')]")))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()