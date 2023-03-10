'''
Created on Nov 20, 2018

@author: ashleyhuey
'''
from shelper.base.TextContext import IText
from shelper.abst.Commands import Commands
from com.utils.Managers import Driver
from selenium.webdriver.support.select import By

class Text(IText):
    
    def get_from(self, element, attribute=""):
        if hasattr(element, "by"):
            return Commands.get_element(element).text
        else:
            return element.text
            
    def is_displayed(self, element, text, attribute=""):
        result = False
        actual_text = None
        if hasattr(element, "by"):
            actual_text = Commands.get_element(element).text.strip().replace("\r\n", " ")
        else:
            actual_text = element.text.strip()
        if actual_text.lower() == text.lower():
            result = True
        return result
    
class JSText(IText):
    
    def get_from(self, element, attribute=""):
        value = ""
        if hasattr(element, "by"):
            if element.by() == By.CSS_SELECTOR:
                value = Driver.driver().execute_script("return document.querySelector('" + element.locator() + "').value")
            elif element.by() == By.ID:
                value = Driver.driver().execute_script("return document.getElementById('" + element.locator() + "').value")
            elif element.by() == By.CLASS_NAME:
                value = Driver.driver().execute_script("return document.getElementsByClassName('" + element.locator() + "').value")
            elif element.by() == By.NAME:
                value = Driver.driver().execute_script("return document.getElementsByName('" + element.locator() + "').value")
            elif element.by() == By.TAG_NAME:
                value = Driver.driver().execute_script("return document.getElementsByTagName('" + element.locator() + "').value")
        else:
            value = Driver.driver().execute_script("return arguments[0].value", element)
        return value
    
    def is_displayed(self, element, text, attribute=""):
        pass
    
class AttributeText(IText):
    
    def get_from(self, element, attribute=""):
        if hasattr(element, "by"):
            return Commands.get_element(element).get_attribute(attribute)
        else:
            return element.get_attribute(attribute)
        
    def is_displayed(self, element, text, attribute=""):
        result = False
        actual_text = None
        if hasattr(element, "by"):
            actual_text = Commands.get_element(element).get_attribute(attribute).strip().lower()
        else:
            actual_text = element.get_attribute(attribute).strip().lower()
        if result is not None and text in actual_text:
            result = True
        return result
    
            
        