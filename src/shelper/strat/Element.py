'''
Created on Nov 26, 2018

@author: ashleyhuey
'''
from shelper.base.ElementContext import IElement
from shelper.abst.Commands import Commands
from com.utils.Managers import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException

class Element(IElement):

    def get(self, element):
        return Commands.get_element(element)
    
    def get_list_of(self, element):
        return Commands.get_elements(element)
    
    def is_displayed(self, element, i):
        if hasattr(element, "by"):    
            try: WebDriverWait(Driver.driver(), i).until(EC.presence_of_element_located((element.by(), element.locator())))
            except WebDriverException:
                return False
            else:
                return True
        else:
            return True
        
    def find(self, first_element, second_element):
        element1 = first_element
        if hasattr(first_element, "by"):
            element1 = Commands.get_element(first_element)
        element1.find_element(second_element)
        
    def find_list_of(self, first_element, second_element):
        element1 = first_element
        if hasattr(first_element, "by"):
            element1 = Commands.get_element(first_element)
        element1.find_elements(second_element)
        
    def is_attribute_present(self, element, attribute):
        result = False
        element1 = element
        if hasattr(element, "by"):
            element1 = Commands.get_element(element)
        try: value = element1.get_attribute(attribute)
        except Exception:
            result = False
        else:
            if value is not None:
                result = True
        return result
            
    def is_enabled(self, element):
        result = False
        element1 = element
        if hasattr(element, "by"):
            element1 = Commands.get_element(element)
        if element1.is_enabled():
            result = True
        return result