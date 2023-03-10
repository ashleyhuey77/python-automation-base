'''
Created on Nov 20, 2018

@author: ashleyhuey
'''
import abc

class IText(object):

    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def get_from(self, element, attribute=""):
        pass
    
    @abc.abstractmethod
    def is_displayed(self, element, text, attribute=""):
        pass
    
class TextContext:
    
    __strategy = ""
    
    def __init__(self, strategy):
        TextContext.__strategy = strategy()

    def get_from(self, element, attribute=""):
        return TextContext.__strategy.get_from(element, attribute)
    
    def is_displayed(self, element, text, attribute=""):
        return TextContext.__strategy.is_displayed(element, text, attribute)