'''
Created on Nov 27, 2018

@author: ashleyhuey
'''
import abc

class IActions(object):
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def move_to(self, element):
        pass
        
    @abc.abstractmethod
    def mouse_over(self, element):
        pass
    
    @abc.abstractmethod
    def drag_and_drop(self, first_element, second_element):
        pass
    
    @abc.abstractmethod
    def scroll_to(self, element):
        pass
    
    @abc.abstractmethod
    def select_from_dropdown(self, element, value, select_type):
        pass
    
class ActionsContext:
    
    __strategy = ""
    
    def __init__(self, strategy):
        ActionsContext.__strategy = strategy()
        
    def move_to(self, element):
        ActionsContext.__strategy.move_to(element)
        
    def mouse_over(self, element):
        ActionsContext.__strategy.mouse_over(element)
        
    def drag_and_drop(self, first_element, second_element):
        ActionsContext.__strategy.drag_and_drop(first_element, second_element)
        
    def scroll_to(self, element):
        ActionsContext.__strategy.scroll_to(element)
    
    def select_from_dropdown(self, element, value, select_type):
        ActionsContext.__strategy.select_from_dropdown(element, value, select_type)

    