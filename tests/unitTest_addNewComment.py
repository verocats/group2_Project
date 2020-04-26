import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/users/krish/OneDrive/Documents/GitHub/CMS_Clients1/tests/chromedriver_win32/chromedriver')


    def test_something(self):
        user = "Krishi"
        pwd = "krishi"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/users/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(3)
        try:
            # click the View All Clients button
            elem = driver.find_element_by_xpath("/html/body/div/div/p[2]/a").click()
            time.sleep(3)
            # find the 'Add comment' button - if client available, Add Comment Button is displayed
            elem = driver.find_element_by_xpath("/html/body/div/div[1]/p/a[3]").click()
            time.sleep(3)
            elem = driver.find_element_by_id("id_client")
            elem.send_keys("Client1")
            elem = driver.find_element_by_id("id_comment")
            elem.send_keys("Unit Test comment")
            elem = driver.find_element_by_id("id_author")
            elem.send_keys("Krishna")
            elem = driver.find_element_by_xpath("/html/body/div/form/button").click()

            assert True
        except NoSuchElementException:
            self.fail("All Clients are not available")
            assert False
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
