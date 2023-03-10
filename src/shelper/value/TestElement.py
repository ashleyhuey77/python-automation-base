'''
Created on Nov 20, 2018

@author: ashleyhuey
'''

class TestElement(object):
    
    __locator = ""
    __by = ""
    
    def __init__(self, locator, by):
        TestElement.__locator = locator
        TestElement.__by = by

    def locator(self):
        return TestElement.__locator
    
    def by(self):
        return TestElement.__by