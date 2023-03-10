'''
Created on Nov 27, 2018

@author: ashleyhuey
'''
from shelper.base.ActionsContext import IActions
from selenium.webdriver.common.action_chains import ActionChains
from com.utils.Managers import Driver
from shelper.abst.Commands import Commands
from log.TestException import TestException
import time
from shelper.Enums import SelectType
from selenium.webdriver.support.ui import Select

class Actions(IActions):
    
    def __selenium_drag_and_drop(self, drag_element, drop_element):
        actions = ActionChains(Driver.driver())
        actions.click_and_hold(drag_element).perform()
        time.sleep(3)
        actions.move_to_element(drop_element).perform()
        time.sleep(3)
        actions.release(drag_element).perform()
        time.sleep(3)
    
    def __select_option(self, select, value, select_type):
        if select_type == SelectType.BY_VALUE:
            select.select_by_value(value)
        elif select_type == SelectType.BY_VISIBLE_TEXT:
            select.select_by_visible_text(value)
        elif select_type == SelectType.BY_INDEX:
            select.select_by_index(value)

    def move_to(self, element):
        if hasattr(element, "by"):
            ActionChains(Driver.driver()).move_to_element(Commands.get_element(element)).perform()
        else:
            ActionChains(Driver.driver()).move_to_element(element).perform()
    
    def mouse_over(self, element):
        if hasattr(element, "by"):
            ActionChains(Driver.driver()).move_to_element(Commands.get_element(element)).hover.perform()
        else:
            ActionChains(Driver.driver()).move_to_element(element).hover.perform()
            
    def drag_and_drop(self, first_element, second_element):
        el1 = None
        el2 = None
        if hasattr(first_element, "by"):
            el1 = Commands.get_element(first_element)
        else:
            raise TestException("Please only provide TestElements not WebElements for drag and drop.")
        if hasattr(second_element, "by"):
            el2 = Commands.get_element(second_element)
        else:
            raise TestException("Please only provide TestElements not WebElements for drag and drop.")
        self.__selenium_drag_and_drop(el1, el2)
        
    def scroll_to(self, element):
        if hasattr(element, "by"):
            element = Commands.get_element(element)
        Driver.driver().execute_script("arguments[0].scrollIntoView();", element)
        
    def select_from_dropdown(self, element, value, select_type):
        if hasattr(element, "by"):
            element = Commands.get_element(element)
        select = Select(element)
        self.__select_option(select, value, select_type)
    
        