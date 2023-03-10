'''
Created on Nov 27, 2018

@author: ashleyhuey
'''
import abc
import shelper.Enums as c

class IWait(object):
    
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        pass

    @abc.abstractmethod
    def on(self, element):
        pass
    
class WaitBuilder:
    
    base_time = 0
    base_condition = c.Condition.INVALID_CONDITION
    base_value = None
    base_exp_total_count = 0
    base_attribute = None
    
    @staticmethod
    def with_a_count_of(value):
        WaitBuilder.base_exp_total_count = value
        return WaitBuilder
    
    @staticmethod
    def for_a_max_time_of(value):
        WaitBuilder.base_time = value
        return WaitBuilder
    
    @staticmethod
    def for_attribute(value):
        WaitBuilder.base_attribute = value
        return WaitBuilder
    
    @staticmethod
    def to(value):
        WaitBuilder.base_condition = value
        return WaitBuilder
    
    @staticmethod
    def value(v):
        WaitBuilder.base_value = v
        return WaitBuilder
    
class WaitContext:
    
    __strategy = ""
    
    def __init__(self, strategy):
        WaitContext.__strategy = strategy
        
    def on(self, element):
        WaitContext.__strategy.on(element)
        