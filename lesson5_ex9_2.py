import unittest
import time
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

    def test_sorting_geozones(self):
        self.driver.find_element_by_xpath("//span[text()='Geo Zones']").click()
        rows = self.driver.find_elements_by_xpath("//tr[@class='row']/td[3]")

        countries_names = []

        for row in rows:
            countries_names.append(row.text)

        for country in countries_names:
            self.driver.find_element_by_xpath("//a[text()='%s']" % country).click()
            print("Checking %s. Please wait..." % country)
            time.sleep(5)
            zones_list = []
            if country == "European Union":
                zones_list = self.driver.find_elements_by_xpath("//tr/td[2]/select[contains(@name,'zones')]/option[@selected='selected']") 
            else:
                zones_list = self.driver.find_elements_by_xpath("//tr/td[3]/select[contains(@name,'zones')]/option[@selected='selected']")

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