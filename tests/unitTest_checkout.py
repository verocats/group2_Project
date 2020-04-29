import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class CMS_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        user = "Krishna"
        pwd = "django123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://europescorner.pythonanywhere.com/")
        time.sleep(3)
        elem = driver.find_element_by_xpath("//*[@id='navbarCollapse']/form/a[1]").click()
        time.sleep(5)

        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        try:

            elem = driver.find_element_by_xpath("//*[@id='main']/div[1]/div/div[1]/a").click()
            time.sleep(3)
            elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/input[3]").click()
            time.sleep(3)
            elem = driver.find_element_by_xpath("/html/body/div[2]/p/a[2]").click()
            time.sleep(3)
            elem = driver.find_element_by_id("id_first_name")
            elem.send_keys("Selenium")
            elem = driver.find_element_by_id("id_last_name")
            elem.send_keys("Testing")
            elem = driver.find_element_by_id("id_address")
            elem.send_keys("1234 Main St")
            elem = driver.find_element_by_id("id_postal_code")
            elem.send_keys("68106")
            elem = driver.find_element_by_id("id_city")
            elem.send_keys("Omaha")
            elem = driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/input[1]")
            elem.send_keys("1234567890")
            elem = driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/input[2]")
            elem.send_keys("112")
            elem = driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/input[3]")
            elem.send_keys("4")
            elem = driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/input[4]")
            elem.send_keys("2020")
            # click the place order button
            elem = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/p/input").click()
            time.sleep(4)
            elem = driver.find_element_by_xpath("/html/body/div[2]/p")
            assert True

        except NoSuchElementException:
            self.fail("Checkout failed")
            assert False

        time.sleep(3)

def tearDown(self):
    self.driver.close()

if __name__ == '__main__':
    unittest.main()
