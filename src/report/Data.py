'''
Created on Nov 28, 2018

@author: ashleyhuey
'''

class ReportSettings(object):
    
    generate_html_reports = True
    include_test_data_in_report = True
    take_screenshot_failed_step = True
    take_screenshot_passed_step = True
    
    __report_name = None
    __report_path = None
    __report_type = None
    
    def get_report_name(self):
        return self.__report_name
    
    def get_report_type(self):
        return self.__report_type
    
    def get_report_path(self):
        return self.__report_path
    
    def __init__(self, report_path, report_name, report_type):
        self.__report_name = report_name
        self.__report_path = report_path
        self.__report_type = report_type
        
class TestContent(object):
    
    __test_scenario_name = None
    __browser_name = None
    __url = None
    __heading4 = None
    
    def __init__(self, scenario_name, browser_name, url, heading4=""):
        self.__test_scenario_name = scenario_name
        self.__browser_name = browser_name
        self.__url = url
        self.__heading4 = heading4
        
    def get_test_scenario_name(self):
        return self.__test_scenario_name
    
    def get_browser_name(self):
        return self.__browser_name
        
    def get_url(self):
        return self.__url
    
class TestStepContent(object):
    
    __number = None
    __name = None
    __description = None
    __status = None
    __screenshot_name = None
    
    def __init__(self, name, description, status, screenshot_name="", number=""):
        self.__number = number
        self.__name = name
        self.__description = description
        self.__status = status
        self.__screenshot_name = screenshot_name
        
    def get_number(self):
        return self.__number
    
    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def get_status(self):
        return self.__status
    
    def get_screenshot_name(self):
        return self.__screenshot_name
        