'''
Created on Nov 20, 2018

@author: ashleyhuey
'''

class Driver(object):
    
    __driver = ""
    
    def __init__(self, driver):
        Driver.__driver = driver
        
    @staticmethod  
    def driver():
        return Driver.__driver
    
class Report(object):
    
    __report = None
    
    def __init__(self, report):
        Report.__report = report
        
    @staticmethod
    def get():
        return Report.__report
    
class Validations(object):
    
    __val = None
    
    def __init__(self, validations):
        Validations.__val = validations
        
    @staticmethod
    def get():
        return Validations.__val
        