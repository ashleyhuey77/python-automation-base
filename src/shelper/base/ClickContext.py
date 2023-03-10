'''
Created on Nov 20, 2018

@author: ashleyhuey
'''
import abc

class IClick(object):

    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def on(self, element):
        pass
    
class ClickContext:
    
    __strategy = ""
    
    def __init__(self, strategy):
        ClickContext.__strategy = strategy()

    def on(self, element):
        ClickContext.__strategy.on(element)
        