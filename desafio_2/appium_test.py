import unittest
from appium import webdriver

class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None


    def setUp(self):
        #This
        self.dc['app'] = "C:\odair\desafio_2\app-debug.apk"
        #this 
        self.dc ['appPackage'] = "com.experitest.ExperiBank"
        self.dc['appActivity'] = ".LoginActivity"
        #this
        self.dc['platformName'] = 'Android'
        #dev
        #dev
        self.dc['deviceName'] = 'a3ae1c63'
        #this
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

        def testFirstAutomation(self):
            if len(self.driver.find_elements_by_xpath("//*[@text='OK']")) > 0:
                self.driver.find_elements_by_xpath("//*[@text='OK']").click();
                #
                self.driver.find_elements_by_xpath("//*[@text='Username']").send_keys('company')
                self.driver.find_elements_by_xpath("//*[@text='Passaword']").send_keys('company')
                self.driver.find_elements_by_xpath("//*[@text='Login']").click()
                 