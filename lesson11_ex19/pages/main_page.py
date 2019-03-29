from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def open(self):
        self.driver.get("http://localhost/litecart/en/")

    def find_product(self, product_name):
        self.driver.find_element_by_name("query").send_keys(product_name, Keys.RETURN)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='title' and text()='%s']" % product_name)))
