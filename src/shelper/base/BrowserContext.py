'''
Created on Nov 26, 2018

@author: ashleyhuey
'''
import abc

class IBrowser(object):
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def switch_focus_to(self, browser_object, element=""):
        pass
    
    @abc.abstractmethod
    def close(self):
        pass
    
    @abc.abstractmethod
    def open(self):
        pass
    
    @abc.abstractmethod
    def navigate_to(self, url):
        pass
    
    @abc.abstractmethod
    def wait_for_window_count(self, i, expected_count):
        pass
    
    @abc.abstractmethod
    def back(self):
        pass
    
class BrowserContext:
    
    __strategy = ""
    
    def __init__(self, strategy):
        BrowserContext.__strategy = strategy()
        
    def switch_focus_to(self, browser_object, element=""):
        BrowserContext.__strategy.switch_focus_to(browser_object, element)
        
    def close(self):
        BrowserContext.__strategy.close()
    
    def open(self):
        BrowserContext.__strategy.open()
        
    def navigate_to(self, url):
        BrowserContext.__strategy.navigate_to(url)
        
    def wait_for_window_count(self, i, expected_count):
        BrowserContext.__strategy.wait_for_window_count(i, expected_count)
        
    def back(self):
        BrowserContext.__strategy.back()

    
        