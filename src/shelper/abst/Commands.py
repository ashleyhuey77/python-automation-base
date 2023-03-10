'''
Created on Nov 15, 2018

@author: ashleyhuey
'''
import abc
from com.utils.Managers import Driver

class Commands(object):
    
    __metaclass__ = abc.ABCMeta

    @staticmethod
    @abc.abstractmethod
    def get_element(test_element):
        element = Driver.driver().find_element(test_element.by(), test_element.locator())
        return element
    
    @staticmethod
    @abc.abstractmethod
    def get_elements(test_element):
        element = Driver.driver().find_elements(test_element.by(), test_element.locator())
        return element