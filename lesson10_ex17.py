import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLitecartMainPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://localhost/litecart/admin/login.php")
        cls.driver.find_element_by_name("username").send_keys("admin")
        cls.driver.find_element_by_name("password").send_keys("admin")
        cls.driver.find_element_by_name("remember_me").click()
        cls.driver.find_element_by_name("login").click()

    def test_browser_logs(self):
        self.driver.find_element_by_xpath("//span[text()='Catalog']").click()
        self.driver.find_element_by_xpath("//a[text()='Rubber Ducks']").click()
        self.driver.find_element_by_xpath("//a[text()='Subcategory']").click()
        products_list = self.driver.find_elements_by_xpath("//tr[@class='row']/td[3]/a")
        for product in products_list:
            product.click()
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//h1[@class='title' and text()='%s']"
            self.driver.back
        

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

if __name__ == '__main__':
    unittest.main()