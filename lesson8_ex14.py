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
        cls.driver.get("http://localhost/litecart/admin/login.php")
        cls.driver.find_element_by_name("username").send_keys("admin")
        cls.driver.find_element_by_name("password").send_keys("admin")
        cls.driver.find_element_by_name("remember_me").click()
        cls.driver.find_element_by_name("login").click()

    def test_windows(self):
        wait = WebDriverWait(self.driver, 10)
        
        self.driver.find_element_by_xpath("//span[text()='Countries']").click()
        
        self.driver.find_element_by_xpath("//a[@class='button']").click()
        
        links_list = self.driver.find_elements_by_xpath("//a[i[@class='fa fa-external-link']]")
        main_window = self.driver.current_window_handle
        old_windows = self.driver.window_handles
        for link in links_list:
            link.click()
            wait.until(EC.new_window_is_opened(old_windows))
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(main_window)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()