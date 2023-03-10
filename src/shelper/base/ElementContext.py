'''
Created on Nov 26, 2018

@author: ashleyhuey
'''
import abc

class IElement(object):
    
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self, element):
        pass
    
    @abc.abstractmethod
    def get_list_of(self, element):
        pass
    
    @abc.abstractmethod
    def is_displayed(self, element, i):
        pass
        
    @abc.abstractmethod
    def find(self, first_element, second_element):
        pass
    
    @abc.abstractmethod
    def find_list_of(self, first_element, second_element):
        pass
    
    @abc.abstractmethod
    def is_attribute_present(self, element, attribute):
        pass
    
    @abc.abstractmethod
    def is_enabled(self, element):
        pass
    
class ElementContext:
    
    __strategy = ""
    
    def __init__(self, strategy):
        ElementContext.__strategy = strategy()
        
    def get(self, element):
        return ElementContext.__strategy.get(element)
    
    def get_list_of(self, element):
        return ElementContext.__strategy.get_list_of(element)
        
    def is_displayed(self, element, i):
        return ElementContext.__strategy.is_displayed(element, i)

    def find(self, first_element, second_element):
        return ElementContext.__strategy.find(first_element, second_element)
    
    def find_list_of(self, first_element, second_element):
        return ElementContext.__strategy.find_list_of(first_element, second_element)
        
    def is_attribute_present(self, element, attribute):
        return ElementContext.__strategy.is_attribute_present(element, attribute)
        
    def is_enabled(self, element):
        return ElementContext.__strategy.is_enabled(element)