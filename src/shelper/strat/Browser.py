'''
Created on Nov 26, 2018

@author: ashleyhuey
'''
from shelper.base.BrowserContext import IBrowser
from shelper.Enums import BrowserObject
from com.utils.Managers import Driver
from shelper.abst.Commands import Commands
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

class Browser(IBrowser):
    
    def __switch_to_new_window(self):
        for window in Driver.driver().window_handles:
            Driver.driver().switch_to_window(window)
    
    def __handle_frames(self, element=""):
        if hasattr(element, "by"):
            Driver.driver().switch_to.frame(Commands.get_element(element))
        else:
            Driver.driver().switch_to.frame(element) 
            
    def __window_count(self, expected_count):
        def predicate(driver):
            try: num_of_windows = len(driver.window_handles)
            except StaleElementReferenceException:
                return False
            else:
                if num_of_windows == expected_count:
                    return True
        return predicate        
    
    def switch_focus_to(self, browser_object, element=""):
        if browser_object == BrowserObject.DEFAULT_CONTENT:
            Driver.driver().switch_to.default_content()
        elif browser_object == BrowserObject.NEW_WINDOW:
            self.__switch_to_new_window()
        elif browser_object == BrowserObject.FRAME:
            self.__handle_frames(self, element)
        elif browser_object == BrowserObject.ALERT:
            Driver.driver().switch_to_alert().accept()
            
    def close(self):
        original_handle = Driver.driver().current_window_handle
        for handle in Driver.driver().window_handles:
            if handle != original_handle:
                Driver.driver().switch_to_window(handle)
                Driver.driver().close()
        Driver.driver().switch_to_window(original_handle)
    
    def open(self):
        Driver.driver().execute_script("window.open();")
        
    def navigate_to(self, url):
        Driver.driver().get(url)
        
    def wait_for_window_count(self, i, expected_count):
        WebDriverWait(Driver.driver(), timeout=i).until(self.__window_count(expected_count))
        
    def back(self):
        Driver.driver().execute_script("window.history.go(-1)")
            

    
        