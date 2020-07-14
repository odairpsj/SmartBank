import unittest
from appium import webdriver

import self as self


class TestMobile(unittest.TestCase):
    dc = {}
    driver = None


    def setUp(self):
        self.dc['app'] = 'c:\\app-debug.apk'
        self.dc['appPackage'] = "com.experitest.ExperiBank"
        self.dc['appActivity'] = ".LoginActivity"
        self.dc['platformName'] = 'Android'
        self.dc['deviceName'] = 'LG K11+'
        self.driver = webdriver.Remote('http://localhost:3000/wd/hub', self.dc)

    def testFirstAutomationTest(self):
        if len(self.driver.find_elements_by_xpath(" // *[@ text=’OK’]")) > 0:
            self.driver.find_element_by_xpath(" // *[ @ text =’OK’]").click();

        self.driver.find_element_by_xpath("//*[ @text =’Username’]").send_keys('company')
        self.driver.find_element_by_xpath("//*[ @text ='Password']").send_keys('company')
        self.driver.find_element_by_xpath("//*[ @text = 'Login']").click()

pass
def tearDown(self):
    self.driver.quit()
