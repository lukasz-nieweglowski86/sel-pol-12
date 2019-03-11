import unittest
from selenium import webdriver

class TestLitecartAdminPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://localhost/litecart/en/")

    def test_product_page(self):
        first_product_in_category = self.driver.find_element_by_xpath("//div[@id='box-campaigns']/div/ul/li")

        product_name = self.driver.find_element_by_xpath("").get_attribute("textContent")
        product_regular_price = self.driver.find_element_by_xpath("").get_attribute("textContent")
        product_campaign_price = self.driver.find_element_by_xpath("").get_attribute("textContent")
        
        first_product_in_category.click()

        subcategory_product_name = self.driver.find_element_by_xpath("//h1[@class='title']").text
        subcategory_product_regular_price = self.driver.find_element_by_xpath("//s[@class='regular-price']").text
        subcategory_product_campaign_price = self.driver.find_element_by_xpath("//strong[@class='campaign-price']").text

        print("Product name is %s." % product_name)
        print("Product regular price is %s." % product_regular_price)
        print("Product campaign price is %s." % product_campaign_price)
        print("Subcategory product name is %s." % subcategory_product_name)
        print("Subcategory product regular price is %s." % subcategory_product_regular_price)
        print("Subcategory product campaign price is %s." % subcategory_product_campaign_price)

        if product_name == subcategory_product_name:
            print("Name is the same on both pages.")
        else:
            print("Name is not the same on both pages.")
        
        if product_regular_price == subcategory_product_regular_price:
            print("Regular price is the same on both pages.")
        else:
            print("Regular price is not the same on both pages.")

        if product_campaign_price == subcategory_product_campaign_price:
            print("Campaign price is the same on both pages.")
        else:
            print("Campaign price is not the same on both pages.")

        

 



        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()