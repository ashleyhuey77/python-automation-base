'''
Created on Nov 20, 2018

@author: ashleyhuey
'''
from aetypes import Enum

class Via(Enum):
    
    SELENIUM = 1
    JAVASCRIPT = 2
    JQUERY = 3

class Variable(Enum):
    
    ATTRIBUTE = 1
    ELEMENT = 2
    
class BrowserObject(Enum):
    
    NEW_WINDOW = 1 
    TAB = 2 
    DEFAULT_CONTENT = 3
    FRAME = 4
    ALERT = 5
    
class Location(Enum):
    
    TOP_OF_PAGE = 1
    BOTTOM_OF_PAGE = 2
    RIGHT_OF_PAGE = 3
    LEFT_OF_PAGE = 4
    
class SelectType(Enum):

    BY_VALUE = 1 
    BY_VISIBLE_TEXT = 2
    BY_INDEX = 3
    
class Wait(Enum):
    
    PRESENCE_OF_ELEMENT = 1
    PRESENCE_OF_ELEMENT_TEXT = 2
    ELEMENT_NOT_TO_BE_PRESENT = 3
    ELEMENT_TEXT_NOT_TO_BE_PRESENT = 4
    PRESENCE_OF_ATTRIBUTE = 5
    PRESENCE_OF_ATTRIBUTE_TEXT = 6
    ATTRIBUTE_NOT_TO_BE_PRESENT = 7
    ATTRIBUTE_TEXT_NOT_TO_BE_PRESENT = 8
    CLICKABILITY_OF_ELEMENT = 9
    COUNT_OF_ELEMENTS = 10
    
class Condition(Enum):
    
    EQUAL = 1
    CONTAIN = 2
    INVALID_CONDITION = 3
        