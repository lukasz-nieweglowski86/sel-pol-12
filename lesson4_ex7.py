import unittest
from selenium import webdriver

class TestLitecartAdminPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://localhost/litecart/admin/login.php")
        cls.driver.find_element_by_name("username").send_keys("admin")
        cls.driver.find_element_by_name("password").send_keys("admin")
        cls.driver.find_element_by_name("remember_me").click()
        cls.driver.find_element_by_name("login").click()

    # def test_appearence_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Appearence']").click()
    #     self.driver.find_element_by_id("doc-template").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-template").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-logotype").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-logotype").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_catalog_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Catalog']").click()
    #     self.driver.find_element_by_id("doc-catalog").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-catalog").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-product_groups").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-product_groups").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-option_groups").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-option_groups").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-manufacturers").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-manufacturers").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-suppliers").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-suppliers").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-delivery_statuses").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-delivery_statuses").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-sold_out_statuses").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-sold_out_statuses").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-quantity_units").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-quantity_units").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-csv").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-csv").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_countries_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Countries']").click()
    #     self.assertEqual(self.driver.find_element_by_xpath("//span[text()='Countries']").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_currencies_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Currencies']").click()
    #     self.assertEqual(self.driver.find_element_by_xpath("//span[text()='Currencies']").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_customers_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Customers']").click()
    #     self.driver.find_element_by_id("doc-customers").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-customers").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-csv").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-csv").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-newsletter").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-newsletter").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_geozones_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Geo Zones']").click()
    #     self.assertEqual(self.driver.find_element_by_xpath("//span[text()='Geo Zones']").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_languages_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Languages']").click()
    #     self.driver.find_element_by_id("doc-languages").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-languages").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-storage_encoding").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-storage_encoding").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_modules_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Modules']").click()
    #     self.driver.find_element_by_id("doc-jobs").click()
    #     self.assertEqual("Job Modules", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-customer").click()
    #     self.assertEqual("Customer Modules", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-shipping").click()
    #     self.assertEqual("Shipping Modules", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-payment").click()
    #     self.assertEqual("Payment Modules", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-order_total").click()
    #     self.assertEqual("Order Total Modules", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-order_success").click()
    #     self.assertEqual("Order Success Modules", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-order_action").click()
    #     self.assertEqual("Order Action Modules", self.driver.find_element_by_xpath("//h1").text)

    # def test_orders_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Orders']").click()
    #     self.driver.find_element_by_id("doc-orders").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-orders").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-order_statuses").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-order_statuses").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_pages_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Pages']").click()
    #     self.assertEqual(self.driver.find_element_by_xpath("//span[text()='Pages']").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_reports_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Reports']").click()
    #     self.driver.find_element_by_id("doc-monthly_sales").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-monthly_sales").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-most_sold_products").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-most_sold_products").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-most_shopping_customers").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-most_shopping_customers").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_settings_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Settings']").click()
    #     self.driver.find_element_by_id("doc-store_info").click()
    #     self.assertEqual("Settings", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-defaults").click()
    #     self.assertEqual("Settings", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-general").click()
    #     self.assertEqual("Settings", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-listings").click()
    #     self.assertEqual("Settings", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-images").click()
    #     self.assertEqual("Settings", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-checkout").click()
    #     self.assertEqual("Settings", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-advanced").click()
    #     self.assertEqual("Settings", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-security").click()
    #     self.assertEqual("Settings", self.driver.find_element_by_xpath("//h1").text)

    # def test_slides_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Slides']").click()
    #     self.assertEqual(self.driver.find_element_by_xpath("//span[text()='Slides']").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_tax_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Tax']").click()
    #     self.driver.find_element_by_id("doc-tax_classes").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-tax_classes").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-tax_rates").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-tax_rates").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_translations_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Translations']").click()
    #     self.driver.find_element_by_id("doc-search").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-search").text, self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-scan").click()
    #     self.assertEqual("Scan Files For Translations", self.driver.find_element_by_xpath("//h1").text)
    #     self.driver.find_element_by_id("doc-csv").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-csv").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_users_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='Users']").click()
    #     self.assertEqual(self.driver.find_element_by_xpath("//span[text()='Users']").text, self.driver.find_element_by_xpath("//h1").text)

    # def test_vqmods_category(self):
    #     self.driver.find_element_by_xpath("//span[text()='vQmods']").click()
    #     self.driver.find_element_by_id("doc-vqmods").click()
    #     self.assertEqual(self.driver.find_element_by_id("doc-vqmods").text, self.driver.find_element_by_xpath("//h1").text)

    def test_categories(self):
        category_count = len(self.driver.find_elements_by_xpath("//li[contains(@id,'app-')]"))
        for i in range(1,category_count+1):
            self.driver.find_element_by_xpath("//li[contains(@id,'app-')][%s]" % i).click()
            subcategory_count = len(self.driver.find_elements_by_xpath("//li[contains(@id,'doc-')]"))
            if subcategory_count > 0:
                for j in range(1,subcategory_count+1):
                    self.driver.find_element_by_xpath("//li[contains(@id,'doc-')][%s]" % j).click()
                    subcategory_name = self.driver.find_element_by_xpath("//li[contains(@id,'doc-')][%s]" % j).text
                    if subcategory_name == self.driver.find_element_by_xpath("//h1").text:
                        print(subcategory_name + " - Category name is the same as h1.")
                    else:
                        print(subcategory_name + " - Category name is not the same as h1.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()