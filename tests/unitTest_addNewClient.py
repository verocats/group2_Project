import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class CMS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/users/krish/OneDrive/Documents/GitHub/CMS_Clients1/tests/chromedriver_win32/chromedriver')

    def test_cms(self):
        #login from the admin pane
        user = "Krishna"
        pwd = "django123"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(5)

        # find the ‘+ New’ and click it
        elem = driver.find_element_by_xpath("/html/body/nav/ul/li/a").click()
        time.sleep(5)
        continue_test = False
        try:
          #verify New Client exists on new screen after clicking "+ New" button
            elem = driver.find_element_by_xpath("/html/body/div/h1").click()
            continue_test = True

        except NoSuchElementException:
            self.fail("Add new client does not appear = New Client button not present")
            assert False
            time.sleep(1)
        except:
            self.fail("Edit post NOT successful - error occurred: ")
            assert False
            time.sleep(1)
        time.sleep(2)
        #if test successful so far – set up the required inputs for a Client
        if continue_test:
            elem = driver.find_element_by_id("id_name")
            elem.send_keys("Test Name")
            elem = driver.find_element_by_id("id_notes")
            elem.send_keys("This is a test note via Selenium testing")
            elem = driver.find_element_by_id("id_address")
            elem.send_keys("1234 Main St")
            elem = driver.find_element_by_id("id_city")
            elem.send_keys("Omaha")
            elem = driver.find_element_by_id("id_state")
            elem.send_keys("") # use default value
            elem = driver.find_element_by_id("id_zipcode")
            elem.send_keys("") #use default
            elem = driver.find_element_by_id("id_email")
            elem.send_keys("testEmail@test.com")
            elem = driver.find_element_by_id("id_cell_phone")
            elem.send_keys("")  #use default value
            elem = driver.find_element_by_id("id_acct_number")
            elem.send_keys("1")
            time.sleep(6)
            #click the Save button
            elem = driver.find_element_by_xpath("/html/body/div/form/button").click()
            time.sleep(6)
            try:

                # find the 'Edit' button - if client added, Edit | Delete are displayed
                elem = driver.find_element_by_xpath("/html/body/div/p[1]/a[1]")
                assert True
            except NoSuchElementException:
                self.fail("Add Client NOT successful")
                assert False
            time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
