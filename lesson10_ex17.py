import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestLitecartMainPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://localhost/litecart/admin/login.php")
        cls.driver.find_element_by_name("username").send_keys("admin")
        cls.driver.find_element_by_name("password").send_keys("admin")
        cls.driver.find_element_by_name("remember_me").click()
        cls.driver.find_element_by_name("login").click()

    def test_browser_logs(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element_by_xpath("//span[text()='Catalog']").click()
        self.driver.find_element_by_xpath("//a[text()='Rubber Ducks']").click()
        self.driver.find_element_by_xpath("//a[text()='Subcategory']").click()

        links_list = len(self.driver.find_elements_by_xpath("//tr/td[3]/a"))
        for i in range(1,links_list):
            i.click()
            print("Link clicked.")
            self.driver.back()

        # self.driver.find_element_by_xpath("//a[text()='Blue Duck']").click()
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//td[@id='content']/h1")))
        # log_data = self.driver.get_log('browser')
        # if len(log_data) > 0:
        #     print(log_data)
        # else:
        #     print("No browser log.")
        # self.driver.back()

        # self.driver.find_element_by_xpath("//a[text()='Green Duck']").click()
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//td[@id='content']/h1")))
        # log_data = self.driver.get_log('browser')
        # if len(log_data) > 0:
        #     print(log_data)
        # else:
        #     print("No browser log.")
        # self.driver.back()

        # self.driver.find_element_by_xpath("//a[text()='Purple Duck']").click()
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//td[@id='content']/h1")))
        # log_data = self.driver.get_log('browser')
        # if len(log_data) > 0:
        #     print(log_data)
        # else:
        #     print("No browser log.")
        # self.driver.back()

        # self.driver.find_element_by_xpath("//a[text()='Red Duck']").click()
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//td[@id='content']/h1")))
        # log_data = self.driver.get_log('browser')
        # if len(log_data) > 0:
        #     print(log_data)
        # else:
        #     print("No browser log.")
        # self.driver.back()

        # self.driver.find_element_by_xpath("//a[text()='Yellow Duck']").click()
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//td[@id='content']/h1")))
        # log_data = self.driver.get_log('browser')
        # if len(log_data) > 0:
        #     print(log_data)
        # else:
        #     print("No browser log.")
        # self.driver.back()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()