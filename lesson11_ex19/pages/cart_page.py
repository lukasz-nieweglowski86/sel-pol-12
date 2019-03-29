from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CartPage(BasePage):

    def checkout(self):
        self.driver.find_element_by_xpath("//a[text()='Checkout »']").click()

    def remove_items(self):
        products_in_cart = len(self.driver.find_elements_by_xpath("//ul[@class='shortcuts']/li"))
        for i in range(0, products_in_cart):
            ducks_name = self.driver.find_element_by_xpath("//p[@style='margin-top: 0px;']/a/strong")            
            self.driver.find_element_by_name("remove_cart_item").click()
            self.wait.until(EC.staleness_of(ducks_name))