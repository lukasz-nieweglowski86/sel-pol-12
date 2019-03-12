import unittest
from selenium import webdriver

class TestLitecartAdminPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://localhost/litecart/en/")

    def test_product_page(self):
        first_product_in_category = self.driver.find_element_by_xpath("//div[@id='box-campaigns']/div/ul/li")

        product_name = self.driver.find_element_by_xpath("//div[@id='box-campaigns']//div[@class='name']").get_attribute("textContent")
        product_regular_price = self.driver.find_element_by_xpath("//div[@id='box-campaigns']//s[@class='regular-price']").get_attribute("textContent")
        product_campaign_price = self.driver.find_element_by_xpath("//div[@id='box-campaigns']//strong[@class='campaign-price']").get_attribute("textContent")
        product_regular_price_color = self.driver.find_element_by_xpath("//div[@id='box-campaigns']//s[@class='regular-price']").value_of_css_property("color")
        product_campaign_price_color = self.driver.find_element_by_xpath("//div[@id='box-campaigns']//strong[@class='campaign-price']").value_of_css_property("color")
        product_regular_price_font_weight = self.driver.find_element_by_xpath("//div[@id='box-campaigns']//s[@class='regular-price']").value_of_css_property("font-weight")
        product_campaign_price_font_weight = self.driver.find_element_by_xpath("//div[@id='box-campaigns']//strong[@class='campaign-price']").value_of_css_property("font-weight")
        product_regular_price_tag = self.driver.find_element_by_xpath("//div[@id='box-campaigns']//s[@class='regular-price']").get_attribute("tagName")
                
        first_product_in_category.click()

        subcategory_product_name = self.driver.find_element_by_xpath("//h1[@class='title']").text
        subcategory_product_regular_price = self.driver.find_element_by_xpath("//s[@class='regular-price']").text
        subcategory_product_campaign_price = self.driver.find_element_by_xpath("//strong[@class='campaign-price']").text
        subcategory_product_regular_price_color = self.driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("color")
        subcategory_product_campaign_price_color = self.driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("color")
        subcategory_product_regular_price_font_weight = self.driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("font-weight")
        subcategory_product_campaign_price_font_weight = self.driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("font-weight")
        subcategory_product_regular_price_tag = self.driver.find_element_by_xpath("//s[@class='regular-price']").get_attribute("tagName")
        
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
        
        if product_regular_price_color == subcategory_product_regular_price_color:
            print("Regular price color is the same on both pages.")
        else:
            print("Regular price color is not the same on both pages.")

        if product_campaign_price_color == subcategory_product_campaign_price_color:
            print("Campaign price color is the same on both pages.")
        else:
            print("Campaign price color is not the same on both pages.")

        if product_regular_price_font_weight == subcategory_product_regular_price_font_weight:
            print("Font weight of products regular price is the same on both pages.")
        else:
            print("Font weight of products regular price is not the same on both pages.")

        if product_campaign_price_font_weight == subcategory_product_campaign_price_font_weight:
            print("Font weight of products campaign price is the same on both pages.")
        else:
            print("Font weight of products campaign price is not the same on both pages.")

        if product_regular_price_tag == subcategory_product_regular_price_tag:
            print("Regular price tag is the same on both pages.")
        else:
            print("Regular price tag is not the same on both pages.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()