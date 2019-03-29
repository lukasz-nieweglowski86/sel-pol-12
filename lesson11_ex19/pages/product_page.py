from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def adding_to_cart(self, quantity):
        self.driver.find_element_by_name("quantity").clear()
        self.driver.find_element_by_name("quantity").send_keys(quantity)
        amount_in_cart = self.driver.find_element_by_xpath("//span[@class='quantity']").get_attribute("textContent")
        self.driver.find_element_by_name("add_cart_product").click()
        self.wait.until_not(EC.text_to_be_present_in_element((By.XPATH, "//span[@class='quantity']"), amount_in_cart))
       