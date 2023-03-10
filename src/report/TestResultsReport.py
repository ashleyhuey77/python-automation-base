# -*- coding: utf-8 -*-
'''
Created on Nov 29, 2018

@author: ashleyhuey
'''
import os
from bs4 import BeautifulSoup
import datetime

class TestResultsReport(object):
    
    __result_summary_path = None
    __report = None
    __html_file = None
    __css_file = None
    __html_soup = None
    __css_soup = None

    def __init__(self, report_settings):
        report_path = report_settings.get_report_path() + os.sep + "HTML Results" + os.sep + report_settings.get_report_name() + ".html"
        self.__result_summary_path = report_path
        
    def __initialize_html(self):
        with open(os.path.dirname(__file__) + "/HTMLReport.html") as self.__html_file:
            contents = self.__html_file.read()
            self.__html_soup = BeautifulSoup(contents, 'lxml')
            
    def __initialize_css(self):
        with open(os.path.dirname(__file__) + "/reportCss.html") as self.__css_file:
            contents = self.__css_file.read()
            self.__css_soup = BeautifulSoup(contents, 'lxml')
            
    def write_to_report(self):
        with open(self.__result_summary_path, "a+") as self.__report:
            content = str(self.__html_soup.prettify("utf-8"))
            print(content)
            self.__report.write(content)
            
    def __change_base_report_page_text(self, report):
        title = self.__html_soup.find("title")
        test_heading = self.__html_soup.find(id="testHeading")
        browser = self.__html_soup.find(id="browser")
        url = self.__html_soup.find(id="url")
        title.insert(0, report.get_test_scenario_name() + "_" + report.get_browser_name() + " – " + "Automation Execution Results")
        test_heading.insert(0, report.get_test_scenario_name())
        browser.insert(0, report.get_browser_name())
        url.insert(0, report.get_url())
    
    def __create_new_row_in_table(self, tr, class_name, content):
        html = None
        if class_name is None:
            html = BeautifulSoup("<td>" + content + "</td>", 'html.parser')
            tr.insert(0, html.td)
        else:
            html = BeautifulSoup("<td class=\"" + class_name + "\">" + content + "</td>", 'html.parser')
            tr.insert(0, html.td)
        
    def __create_status_row(self, tr, step_no, status, screenshot_name):
        new = BeautifulSoup("<td id=\"" + status + step_no + "\" class=\"" + status + "\"></td>", 'html.parser')
        tr.insert(0, new.td)
        td = self.__html_soup.find(id=status + step_no)
        if status == "PASS":
            pass_img = BeautifulSoup("<img id=\"glass\" align=\"justify\" src=\"../../../../../resources/reportContent/64x64_ICONS_Navigation_Checkmark.jpg\"/>", 'html.parser')
            pass_ss = BeautifulSoup("<a href=\"..\\Screenshots\\" + screenshot_name + "\">" + status + "</a>", 'html.parser')
            td.insert(0, pass_img.img)
            td.insert(0, pass_ss.a)
        elif status == "FAIL":
            fail_img = BeautifulSoup("<img id=\"glass\" align=\"justify\" src=\"../../../../../resources/reportContent/64x64_ICONS_Navigation_Alert.jpg\"/>", 'html.parser')
            fail_ss = BeautifulSoup("<a href=\"..\\Screenshots\\" + screenshot_name + "\">" + status + "</a>", 'html.parser')
            td.insert(0, fail_img.img)
            td.insert(0, fail_ss.a)
        elif status == "DONE":
            done_img = BeautifulSoup("<img id=\"glass\" align=\"justify\" src=\"../../../../../resources/reportContent/64x64_ICONS_Navigation_Checkmark.jpg\"/>", 'html.parser')
            td.insert(0, done_img.img)
            td.insert(0, status.upper())
        elif status == "WARNING":
            warn_img = BeautifulSoup("<img id=\"glass\" align=\"justify\" src=\"../../../../../resources/reportContent/64x64_ICONS_Navigation_Alert.jpg\"/>", 'html.parser')
            td.insert(0, warn_img.img)
            td.insert(0, status.upper())
        
        
    def add_base_report_content(self, report):
        self.__initialize_html()
        self.__initialize_css()
        self.__html_soup.head.insert(0, self.__css_soup)
        self.__change_base_report_page_text(report)
        #self.__write_to_report(str(self.__html_soup))
        
    def add_result_content(self, test_step):
        test_steps_table = self.__html_soup.find(id="testStepsTable")
        html = BeautifulSoup("<tr class=\"content\" id=\"" + test_step.get_number() + "\">", 'html.parser')
        test_steps_table.append(html.tr)
        tr = self.__html_soup.find(id=test_step.get_number())
        self.__create_new_row_in_table(tr, None, datetime.datetime.today().strftime('%I:%M:%S'))
        self.__create_status_row(tr, test_step.get_number(), test_step.get_status(), test_step.get_screenshot_name())
        self.__create_new_row_in_table(tr, "description", test_step.get_description())
        self.__create_new_row_in_table(tr, "justified", test_step.get_name())
        self.__create_new_row_in_table(tr, None, test_step.get_number())
        #self.__write_to_report(str(self.__html_soup.prettify("utf-8")))
        
    def create_directory_path(self):
        with open(self.__result_summary_path, "a+") as file:
            file.write("")
            