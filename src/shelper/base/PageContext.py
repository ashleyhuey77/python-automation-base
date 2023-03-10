'''
Created on Nov 26, 2018

@author: ashleyhuey
'''
import abc

class IPage(object):
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def scroll_to(self, location):
        pass
    
    @abc.abstractmethod
    def refresh(self):
        pass
    
class PageContext:
    
    __strategy = ""
    
    def __init__(self, strategy):
        PageContext.__strategy = strategy()
        
    def scroll_to(self, location):
        PageContext.__strategy.scroll_to(location)
        
    def refresh(self):
        PageContext.__strategy.refresh()