'''
Created on Nov 26, 2018

@author: ashleyhuey
'''
from shelper.base.PageContext import IPage
from shelper.Enums import Location
from com.utils.Managers import Driver

class Page(IPage):
    
    def scroll_to(self, location):
        h_location = "0"
        w_location = "0"
        if location == Location.TOP_OF_PAGE:
            h_location = "-document.body.scrollHeight"
        elif location == Location.BOTTOM_OF_PAGE:
            h_location = "document.body.scrollHeight"
        elif location == Location.RIGHT_OF_PAGE:
            w_location = "document.body.scrollWidth"
        elif location == Location.LEFT_OF_PAGE:
            w_location = "-document.body.scrollWidth"
        Driver.driver().execute_script("window.scrollTo(" + w_location + ", " + h_location + ")")
        
    def refresh(self):
        Driver.driver().refresh()
            