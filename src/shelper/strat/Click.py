'''
Created on Nov 15, 2018

@author: ashleyhuey
'''
from shelper.abst.Commands import Commands
from shelper.base.ClickContext import IClick
from com.utils.Managers import Driver
from selenium.webdriver.support.select import By

class Click(IClick):
  
    def on(self, element):
        if hasattr(element, "by"):
            Commands.get_element(element).click()
        else:
            element.click()
            
class JSClick(IClick):
    
    def on(self, element):
        if hasattr(element, "by"):
            if element.by() == By.CSS_SELECTOR:
                Driver.driver().execute_script("document.querySelector('" + element.locator() + "').click();")
            elif element.by() == By.ID:
                Driver.driver().execute_script("document.getElementById('" + element.locator() + "').click();")
            elif element.by() == By.CLASS_NAME:
                Driver.driver().execute_script("document.getElementsByClassName('" + element.locator() + "').click();")
            elif element.by() == By.NAME:
                Driver.driver().execute_script("document.getElementsByName('" + element.locator() + "').click();")
            elif element.by() == By.TAG_NAME:
                Driver.driver().execute_script("document.getElementsByTagName('" + element.locator() + "').click();")
        else:
            Driver.driver().execute_script("arguments[0].click();", element)
            
class JQClick(IClick):
    
    def on(self, element):
        if hasattr(element, "by"):
            Driver.driver().execute_script("$('" + element.locator() + "').click();")
        else:
            Driver.driver().execute_script("arguments[0].click();", element)