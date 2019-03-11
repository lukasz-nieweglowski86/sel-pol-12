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

    def test_sorting_countries(self):
        self.driver.find_element_by_xpath("//span[text()='Countries']").click()
        countries_list = self.driver.find_elements_by_xpath("//tr/td[5]")

        countries_names = []
        
        for country in countries_list:
            countries_names.append(country.text)

        countries_names_sorted = countries_names[:]
        countries_names_sorted.sort()
        
        if countries_names == countries_names_sorted:
            print("Countries are sorted alphabetically.")
        else:
            print("Countries are not sorted alphabetically.")

        rows = self.driver.find_elements_by_xpath("//tr[@class='row']")
        countries_to_click = []

        for row in rows:
            if row.find_element_by_xpath("td[6]").text != "0":
                countries_to_click.append(row.find_element_by_xpath("td[5]").text)
        for country in countries_to_click:
            self.driver.find_element_by_xpath("//a[text()='%s']" % country).click()

            zones_list = self.driver.find_elements_by_xpath("tr/td[3]")

            zones_names = []

            for zone in zones_list:
                zones_names.append(zone.text)
            
            zones_names_sorted = zones_names[:]
            zones_names_sorted.sort()

            if zones_names == zones_names_sorted:
                print("Zones in %s are sorted alphabetically." % country)
            else:
                print("Zones in %s are not sorted alphabetically." % country)
            self.driver.back()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()