'''
Created on Nov 26, 2018

@author: ashleyhuey
'''
import abc

class IEnter(object):
    
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def text_into(self, element, text):
        pass
    
    @abc.abstractmethod
    def clear(self, element):
        pass
    
class EnterContext:
    
    __strategy = ""
    
    def __init__(self, strategy):
        EnterContext.__strategy = strategy()

    def text_into(self, element, text):
        EnterContext.__strategy.text_into(element, text)
        
    def clear(self, element):
        EnterContext.__strategy.clear(element)
        