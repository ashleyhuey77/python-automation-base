'''
Created on Dec 4, 2018

@author: ashleyhuey
'''
import os
from report.Enums import ReportType, Status
from report.TestResultsReport import TestResultsReport
import datetime
from report.Data import TestStepContent

class ReportTemplate(object):

    __report_settings = None
    __report_content = None
    __n_steps_passed = 0
    __n_steps_failed = 0
    __step_number = None
    __report_types = []
    
    def __init__(self, report_settings):
        self.__report_settings = report_settings
        if report_settings.get_report_type() == ReportType.TEST_RESULTS_REPORT:
            self.__report_content = TestResultsReport(report_settings)
        self.__initialize_report_types()
        self.__create_test_report_file()
            
    def __initialize_report_types(self):
        if self.__report_settings.generate_html_reports:
            results_path = self.__report_settings.get_report_path() + "/" + "HTML Results"
            screenshots_path = self.__report_settings.get_report_path() + "/" + "Screenshots"
            if self.__report_settings.generate_html_reports:
                try:
                    os.makedirs(results_path)
                except:
                    if not os.path.isdir(results_path):
                        raise
                html_report = TestResultsReport(self.__report_settings)
                self.__report_types.append(html_report)
            try:
                os.makedirs(screenshots_path)
            except:
                if not os.path.isdir(screenshots_path):
                    raise
    
    def __create_test_report_file(self):
        for report in self.__report_types:
            self.__report_content.create_directory_path()
            
    def write_to_report(self):
        self.__report_content.write_to_report()
            
    def add_base_report_content(self, report):
        for r in self.__report_types:
            self.__report_content.add_base_report_content(report)
        
    def add_result_content(self, test_step):
        report_path = None
        value = None
        msg = "Screenshots"
        if self.__step_number is None:
            self.__step_number = "1"
        if test_step.get_status() == Status.FAIL.name:
            self.__n_steps_failed = self.__n_steps_failed + 1
            if self.__report_settings.take_screenshot_failed_step:
                value = self.__report_settings.get_report_name() + "_" + datetime.datetime.today().strftime('%m-%d-%y_%I:%M:%S') + ".png"
                report_path = self.__report_settings.get_report_path() + "/" + msg + "/" + value
                self.take_screenshot(report_path)
        elif test_step.get_status() == Status.PASS.name:
            self.__n_steps_passed = self.__n_steps_passed + 1
            if self.__report_settings.take_screenshot_passed_step:
                value = self.__report_settings.get_report_name() + "_" + datetime.datetime.today().strftime('%m-%d-%y_%I:%M:%S') + ".png"
                report_path = self.__report_settings.get_report_path() + "/" + msg + "/" + value
                self.take_screenshot(report_path)
        for r in self.__report_types:
            tsc = TestStepContent(test_step.get_name(), test_step.get_description(), test_step.get_status(), value, self.__step_number)
            self.__report_content.add_result_content(tsc)
        s_num = int(self.__step_number) + 1
        self.__step_number = str(s_num)
                
    def take_screenshot(self, screenshot_path):
        print("Unsupported method in base class")