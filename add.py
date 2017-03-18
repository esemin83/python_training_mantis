# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/mantisbt-1.2.19/login_page.php")
        wd.find_element_by_css_selector("html").click()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("administrator")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("root")
        wd.find_element_by_css_selector("input.button").click()
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_link_text("name2").click()
        wd.find_element_by_xpath("//div[4]/form/input[3]").click()
        wd.find_element_by_css_selector("input.button").click()
        wd.find_element_by_link_text("Logout").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
