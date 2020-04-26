import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class CMS_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/users/krish/OneDrive/Documents/GitHub/CMS_Clients1/tests/chromedriver_win32/chromedriver')

    def test_cms(self):
        user = "Krishi"
        pwd = "krishi"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        try:
            # attempt to find the '+ New' - if found, logged in
            elem = driver.find_element_by_xpath("/html/body/nav/ul/li/a")
            assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(3)

def tearDown(self):
    self.driver.close()

if __name__ == '__main__':
    unittest.main()
