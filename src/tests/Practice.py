'''
Created on Nov 20, 2018

@author: ashleyhuey
'''
import unittest
import os
from selenium import webdriver
from shelper.SHelper import SHelper
from shelper.value.TestElement import TestElement
from selenium.webdriver.support.select import By
from com.utils.Report import ReportHelper, ValidationsHelper
from com.utils.Managers import Driver, Report, Validations
from shelper.Enums import Via, BrowserObject, Wait, Condition
from shelper.Enums import Variable
from shelper.base.WaitContext import WaitBuilder
from com.utils.Report import TestReportHelper

class Test(unittest.TestCase):


    def setUp(self):
        # get the path of ChromeDriverServer
        chrome_driver_path = os.path.dirname(__file__) + "/chromedriver"
        trh = TestReportHelper()
        report = trh.initialize("test_click_method", "Chrome")
        Report(ReportHelper(report))
        Validations(ValidationsHelper(report))
        
        # create a new Chrome session
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
        Driver(driver)
        # navigate to the application home page
        SHelper.browser().navigate_to("http://www.google.com/")
    
    def test_click_method(self):
        displayed_result = SHelper.element().is_displayed(TestElement("q", By.NAME), 3)
        enabled_result = SHelper.element().is_enabled(TestElement("q", By.NAME))
        print(displayed_result)
        print(enabled_result)
        element = SHelper.element().get(TestElement("q", By.NAME))
        SHelper.enter().text_into(element, "Testing")
        SHelper.enter().clear(element)
        SHelper.wait(Wait.PRESENCE_OF_ELEMENT, WaitBuilder.for_a_max_time_of(3)) \
            .on(TestElement("#hptl > a:nth-child(1)", By.CSS_SELECTOR))
        Report.get().report_done_event("Testing report 1")
        SHelper.wait(Wait.ELEMENT_NOT_TO_BE_PRESENT, WaitBuilder.for_a_max_time_of(3)) \
            .on(TestElement("#testing", By.CSS_SELECTOR))
        SHelper.wait(Wait.CLICKABILITY_OF_ELEMENT, WaitBuilder.for_a_max_time_of(3)) \
            .on(TestElement("#hptl > a:nth-child(1)", By.CSS_SELECTOR))
        Validations.get().assertion_pass("Testing assertion pass")
        SHelper.click(Via.SELENIUM).on(TestElement("#hptl > a:nth-child(1)", By.CSS_SELECTOR))
        SHelper.wait(Wait.PRESENCE_OF_ELEMENT, WaitBuilder.for_a_max_time_of(3)) \
            .on(TestElement("a[href='https://www.google.com/doodles']", By.CSS_SELECTOR))
        value = SHelper.text(Variable.ELEMENT, Via.SELENIUM) \
                .get_from(TestElement("body > main > div > div > p", By.CSS_SELECTOR))
        SHelper.wait(Wait.PRESENCE_OF_ELEMENT_TEXT, WaitBuilder
                     .for_a_max_time_of(3)
                     .to(Condition.CONTAIN)
                     .value(value)).on(TestElement("body > main > div > div > p", By.CSS_SELECTOR))
        result = SHelper.text(Variable.ELEMENT, Via.SELENIUM) \
                        .is_displayed(TestElement("a[href='https://www.google.com/doodles']", By.CSS_SELECTOR), "poop")
        attr = SHelper.text(Variable.ATTRIBUTE, Via.SELENIUM) \
                    .get_from(TestElement("a[href='https://www.google.com/doodles']", By.CSS_SELECTOR), "href")
        Validations.get().assertion_pass("Testing assertion pass 2")
        SHelper.wait(Wait.PRESENCE_OF_ATTRIBUTE_TEXT, WaitBuilder.for_a_max_time_of(3)
                     .to(Condition.CONTAIN).value(attr)
                     .for_attribute("href")).on(TestElement("a[href='https://www.google.com/doodles']", By.CSS_SELECTOR))
        attr_result = SHelper.text(Variable.ATTRIBUTE, Via.SELENIUM) \
                            .is_displayed(TestElement("a[href='https://www.google.com/doodles']", By.CSS_SELECTOR), "https://www.google.com/doodles", "href")
        print(value)
        print(result)
        print(attr)
        print(attr_result)
        Report.get().report_done_event("Testing report 2")
        #Validations.get().assertion_failed("This test Failed.")
        SHelper.browser().open()
        SHelper.browser().wait_for_window_count(10, 2)
        SHelper.browser().switch_focus_to(BrowserObject.NEW_WINDOW)
        SHelper.browser().navigate_to("http://www.facebook.com")
        SHelper.browser().close()
        SHelper.browser().wait_for_window_count(10, 1)

    def tearDown(self):
        Report.get().write_report()
        Driver.driver().close()


    def testName(self):
        pass


if __name__ == "__main__":
    unittest.main()