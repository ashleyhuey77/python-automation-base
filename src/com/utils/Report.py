'''
Created on Dec 4, 2018

@author: ashleyhuey
'''
from report.ReportTemplate import ReportTemplate
from com.utils.Managers import Driver
from report.Data import TestStepContent, ReportSettings, TestContent
from report.Enums import Status, ReportType
import inspect
from log.TestException import TestException
import os
import datetime

class TestReport(ReportTemplate):

    def __init__(self, report_settings):
        super(TestReport, self).__init__(report_settings)
        
    def take_screenshot(self, screenshot_path):
        Driver.driver().get_screenshot_as_file(screenshot_path)
        
    def report_done_event(self, step_name, description):
        tsc = TestStepContent(step_name, description, Status.DONE.name)
        super(TestReport, self).add_result_content(tsc)
        
    def report_warning(self, step_name, description):
        tsc = TestStepContent(step_name, description, Status.WARNING.name)
        super(TestReport, self).add_result_content(tsc)
        
    def report_pass_event(self, step_name, description):
        try:
            tsc = TestStepContent(step_name, description, Status.PASS.name)
            super(TestReport, self).add_result_content(tsc)
        except:
            tsc = TestStepContent(step_name, description, Status.WARNING.name)
            super(TestReport, self).add_result_content(tsc)
        
    def report_fail_event(self, step_name, description):
        try:
            tsc = TestStepContent(step_name, description, Status.FAIL.name)
            super(TestReport, self).add_result_content(tsc)
        except:
            tsc = TestStepContent(step_name, description, Status.WARNING.name)
            super(TestReport, self).add_result_content(tsc)
            
    def write_report_content(self):
        super(TestReport, self).write_to_report()
            
class ValidationsHelper(object):
    
    __test_report = None
    
    def __init__(self, html_report):
        self.__test_report = html_report
        
    def assertion_pass(self, msg):
        step_name = inspect.stack()[1][3]
        self.__test_report.report_pass_event(step_name, msg)
        print("Step: " + step_name + " has passed. " + msg)
        
    def assertion_failed(self, msg):
        step_name = inspect.stack()[1][3]
        self.__test_report.report_fail_event(step_name, msg)
        print("Step: " + step_name + " has failed. " + msg)
        raise TestException(msg)
    
class ReportHelper(object):
    
    __test_report = None
    
    def __init__(self, html_report):
        self.__test_report = html_report
        
    def report_done_event(self, msg): 
        step_name = inspect.stack()[1][3]
        self.__test_report.report_done_event(step_name, msg)
        print("Step: " + step_name + " has passed. " + msg)
        
    def report_exception(self, exception):
        step_name = inspect.stack()[1][3]
        self.__test_report.report_fail_event(step_name, str(exception))
        message = "Step: " + step_name + " has failed. \n ErrorMessage: " + str(exception)
        raise TestException(message)
    
    def write_report(self):
        self.__test_report.write_report_content()
    
class ReportPathBuilder(object):
    
    RESULT_FOLDER = "Results"
    __report_path = None
    __instance = None
    
    def __init__(self):
        try:
            os.makedirs(self.RESULT_FOLDER)
        except:
            if not os.path.isdir(self.RESULT_FOLDER):
                raise
        self.__report_path = self.__get_local_report_path()
        os.makedirs(self.__report_path)
            
    def __get_local_report_path(self):
        path = self.RESULT_FOLDER + "/" + "Result_" + datetime.datetime.today().strftime('%m-%d-%y_%I%M%S')
        return path
    
    def get_report_path(self):
        return self.__report_path
    
    @staticmethod
    def get_instance():
        if ReportPathBuilder.__instance is None:
            ReportPathBuilder.__instance = ReportPathBuilder()
        return ReportPathBuilder.__instance
    
class TestReportHelper(object):
    
    def initialize(self, test_scenario_name, browser_name):
        report_file_path = ReportPathBuilder.get_instance().get_report_path()
        file_name = test_scenario_name + "_" + browser_name
        r_settings = ReportSettings(report_file_path, file_name, ReportType.TEST_RESULTS_REPORT)
        t_content = TestContent(test_scenario_name, browser_name, "http://www.google.com")
        r_settings.generate_html_reports = True
        r_settings.include_test_data_in_report = False
        r_settings.take_screenshot_failed_step = True
        r_settings.take_screenshot_passed_step = True
        html_report = TestReport(r_settings)
        html_report.add_base_report_content(t_content)
        return html_report