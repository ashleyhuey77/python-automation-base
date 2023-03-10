'''
Created on Nov 27, 2018

@author: ashleyhuey
'''
from shelper.base.WaitContext import IWait, WaitBuilder
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from com.utils.Managers import Driver
from log.TestException import TestException
from shelper.Enums import Condition
from shelper.SHelper import SHelper
from shelper.Enums import Wait
from shelper.abst.Commands import Commands
from selenium.common.exceptions import StaleElementReferenceException

class ClickableElement(IWait):
    
    __time = 0
    
    def __init__(self, builder):
        super(ClickableElement, self).__init__()
        self.__time = builder.base_time
        if self.__time == 0:
            raise TestException("Time is null. Add the 'forAMaxTimeOf' method.")
        if builder.base_condition != Condition.INVALID_CONDITION:
            raise TestException("Condition is not null. Remove the 'to' method.")
        if builder.base_value is not None:
            raise TestException("Value is not null. Remove the 'value' method.")
        if builder.base_exp_total_count != 0:
            raise TestException("Expected total count is not null. Remove the 'withACountOf' method.")
        if builder.base_attribute is not None:
            raise TestException("Attribute is not null. Remove the 'forAttribute' method.")
        
    def on(self, element):
        WebDriverWait(Driver.driver(), self.__time).until(EC.element_to_be_clickable((element.by(), element.locator())))
        
class ElementCount(IWait):
    
    __time = 0
    __exp_total_count = 0
    
    def __init__(self, builder):
        super(ElementCount, self).__init__()
        self.__exp_total_count = builder.base_exp_total_count
        self.__time = builder.base_time
        if self.__time == 0:
            raise TestException("Time is null. Add the 'forAMaxTimeOf' method.")
        if builder.base_exp_total_count == 0:
            raise TestException("Expected Total Count is null. Add the 'withACountOf' method.")
        if builder.base_condition != Condition.INVALID_CONDITION:
            raise TestException("Condition is not null. Remove the 'to' method.")
        if builder.base_value is not None:
            raise TestException("Value is not null. Remove the 'value' method.")
        if builder.base_attribute is not None:
            raise TestException("Attribute is not null. Remove the 'forAttribute' method.")
    
    def __element_count(self, element, expected_count):
        def predicate(driver):
            result = False
            #SHelper.page().refresh()
            try: SHelper.wait(Wait.PRESENCE_OF_ELEMENT, WaitBuilder.for_a_max_time_of(3)).on(element)
            except Exception:
                return False
            else:
                actual_count = len(element)
                if actual_count == expected_count:
                    result = True
            return result
        return predicate 
    
    def on(self, element):
        if type(element) is not list:
            element = Commands.get_elements(element)
        WebDriverWait(Driver.driver(), timeout=self.__time).until(self.__element_count(element, self.__exp_total_count))
        
class NonPresentAttribute(IWait):
    
    __time = 0
    __attribute = None
    
    def __init__(self, builder):
        super(NonPresentAttribute, self).__init__()
        self.__time = builder.base_time
        self.__attribute = builder.base_attribute
        if self.__time == 0:
            raise TestException("Time is null. Add the 'forAMaxTimeOf' method.")
        if self.__attribute is None:
            raise TestException("Attribute is null. Add the 'forAttribute' method.")
        if builder.base_condition != Condition.INVALID_CONDITION:
            raise TestException("Condition is not null. Remove the 'to' method.")
        if builder.base_value is not None:
            raise TestException("Value is not null. Remove the 'value' method.")
        if builder.base_exp_total_count != 0:
            raise TestException("Expected total count is not null. Remove the 'withACountOf' method.")
    
    def __nonpresence_of_attribute(self, element, attribute):
        def predicate(driver):
            result = False
            value = element.get_attribute(attribute)
            if value is None or value == "":
                result = True
            return result
        return predicate 
    
    def on(self, element):
        if hasattr(element, "by"):
            element = Commands.get_element(element)
        WebDriverWait(Driver.driver(), timeout=self.__time).until(self.__nonpresence_of_attribute(element, self.__attribute))

class NonPresentAttributeText(IWait):
    
    __time = 0
    __condition = None
    __value = None
    __attribute = None

    def __init__(self, builder):
        super(NonPresentAttributeText, self).__init__()
        self.__time = builder.base_time
        self.__condition = builder.base_condition
        self.__value = builder.base_value
        self.__attribute = builder.base_attribute
        if self.__time == 0:
            raise TestException("Time is null. Add the 'forAMaxTimeOf' method.")
        if self.__condition == Condition.INVALID_CONDITION:
            raise TestException("Please select a valid condition. Unable to execute because condition is not valid.")
        if self.__value is None:
            raise TestException("Value is null. Add the 'value' method.")
        if self.__attribute is None:
            raise TestException("Attribute is null. Add the 'forAttribute' method.")
        if builder.base_exp_total_count != 0:
            raise TestException("Expected total count is not null. Remove the 'withACountOf' method.")
        
    def __attribute_to_no_longer_equal_value(self, element, attribute, value):
        def predicate(driver):
            result = False
            actual_value = element.get_attribute(attribute)
            # returning true if attribute is null because it
            # still means the attribute does not contain the
            # desired value.
            if actual_value is None or actual_value.lower() == value.lower():
                result = True
            return result
        return predicate
    
    def __attribute_to_no_longer_contain_value(self, element, attribute, value):
        def predicate(driver):
            result = False
            actual_value = element.get_attribute(attribute)
            # returning true if attribute is null because it
            # still means the attribute does not contain the
            # desired value.
            if actual_value is None or value in actual_value:
                result = True
            return result
        return predicate
    
    def on(self, element):
        if hasattr(element, "by"):
            element = Commands.get_element(element)
        if self.__condition == Condition.CONTAIN:
            WebDriverWait(Driver.driver(), timeout=self.__time).until(self.__attribute_to_no_longer_contain_value(element, self.__attribute, self.__value))
        if self.__condition == Condition.EQUAL:
            WebDriverWait(Driver.driver(), timeout=self.__time).until(self.__attribute_to_no_longer_equal_value(element, self.__attribute, self.__value))
            
class NonPresentElement(IWait):
    
    __time = 0
    
    def __init__(self, builder):
        super(NonPresentElement, self).__init__()
        self.__time = builder.base_time
        if self.__time == 0:
            raise TestException("Time is null. Add the 'forAMaxTimeOf' method.")
        if builder.base_condition != Condition.INVALID_CONDITION:
            raise TestException("Condition is not null. Remove the 'to' method.")
        if builder.base_value is not None:
            raise TestException("Value is not null. Remove the 'value' method.")
        if builder.base_exp_total_count != 0:
            raise TestException("Expected total count is not null. Remove the 'withACountOf' method.")
        if builder.base_attribute is not None:
            raise TestException("Attribute is not null. Remove the 'forAttribute' method.")
        
    def __nonpresent_defined_element(self, element):
        def predicate(driver):
            result = False
            try: element.is_displayed()
            except StaleElementReferenceException:
                result = True
            return result
        return predicate
    
    def on(self, element):
        if hasattr(element, "by"):
            WebDriverWait(Driver.driver(), timeout=self.__time).until(EC.invisibility_of_element_located((element.by(), element.locator())))
        else:
            WebDriverWait(Driver.driver(), timeout=self.__time).until(self.__nonpresent_defined_element(element))
            
class NonPresentElementText(IWait):
    
    __time = 0
    __condition = Condition.INVALID_CONDITION
    __value = None

    def __init__(self, builder):
        super(NonPresentElementText, self).__init__()
        self.__time = builder.base_time
        self.__condition = builder.base_condition
        self.__value = builder.base_value
        if self.__time == 0:
            raise TestException("Time is null. Add the 'forAMaxTimeOf' method.")
        if self.__condition == Condition.INVALID_CONDITION:
            raise TestException("Please select a valid condition. Unable to execute because condition is not valid.")
        if self.__value is None:
            raise TestException("Value is null. Add the 'value' method.")
        if builder.base_attribute is not None:
            raise TestException("Attribute is not null. Remove the 'forAttribute' method.")
        if builder.base_exp_total_count != 0:
            raise TestException("Expected total count is not null. Remove the 'withACountOf' method.")
        
    def __text_to_no_longer_equal_value(self, element, value):
        def predicate(driver):
            result = False
            actual_value = element.text
            if actual_value.lower() != value.lower():
                result = True
            return result
        return predicate
    
    def __text_to_no_longer_contain_value(self, element, value):
        def predicate(driver):
            result = False
            actual_value = element.text
            if value.lower() not in actual_value.lower():
                result = True
            return result
        return predicate
    
    def on(self, element):
        if hasattr(element, "by"):
            element = Commands.get_element(element)
        if self.__condition == Condition.CONTAIN:
            WebDriverWait(Driver.driver(), timeout=self.__time).until(self.__text_to_no_longer_contain_value(element, self.__value))
        if self.__condition == Condition.EQUAL:
            WebDriverWait(Driver.driver(), timeout=self.__time).until(self.__text_to_no_longer_equal_value(element, self.__value))    
            
class PresentAttribute(IWait):
    
    __time = 0
    __attribute = None
    
    def __init__(self, builder):
        super(PresentAttribute, self).__init__()
        self.__time = builder.base_time
        self.__attribute = builder.base_attribute
        if self.__time == 0:
            raise TestException("Time is null. Add the 'forAMaxTimeOf' method.")
        if self.__attribute is None:
            raise TestException("Attribute is null. Add the 'forAttribute' method.")
        if builder.base_condition != Condition.INVALID_CONDITION:
            raise TestException("Condition is not null. Remove the 'to' method.")
        if builder.base_value is not None:
            raise TestException("Value is not null. Remove the 'value' method.")
        if builder.base_exp_total_count != 0:
            raise TestException("Expected total count is not null. Remove the 'withACountOf' method.")
    
    def __presence_of_attribute(self, element, attribute):
        def predicate(driver):
            result = False
            value = element.get_attribute(attribute)
            if value is not None or value != "":
                result = True
            return result
        return predicate 
    
    def on(self, element):
        if hasattr(element, "by"):
            element = Commands.get_element(element)
        WebDriverWait(Driver.driver(), timeout=self.__time).until(self.__presence_of_attribute(element, self.__attribute))
  
class PresentAttributeText(IWait):

    __time = 0
    __condition = None
    __value = None
    __attribute = None

    def __init__(self, builder):
        super(PresentAttributeText, self).__init__()
        self.__time = builder.base_time
        self.__condition = builder.base_condition
        self.__value = builder.base_value
        self.__attribute = builder.base_attribute
        if self.__time == 0:
            raise TestException("Time is null. Add the 'forAMaxTimeOf' method.")
        if self.__condition == Condition.INVALID_CONDITION:
            raise TestException("Please select a valid condition. Unable to execute because condition is not valid.")
        if self.__value is None:
            raise TestException("Value is null. Add the 'value' method.")
        if self.__attribute is None:
            raise TestException("Attribute is null. Add the 'forAttribute' method.")
        if builder.base_exp_total_count != 0:
            raise TestException("Expected total count is not null. Remove the 'withACountOf' method.")

    def __attribute_to_equal_value(self, element, attribute, value):
        def predicate(driver):
            result = False
            actual_value = element.get_attribute(attribute)
            if actual_value.lower() == value.lower():
                result = True
            return result
        return predicate
    
    def __attribute_to_contain_value(self, element, attribute, value):
        def predicate(driver):
            result = False
            actual_value = element.get_attribute(attribute)
            if value in actual_value:
                result = True
            return result
        return predicate
    
    def on(self, element):
        if hasattr(element, "by"):
            element = Commands.get_element(element)
        if self.__condition == Condition.CONTAIN:
            WebDriverWait(Driver.driver(), timeout=self.__time).until(self.__attribute_to_contain_value(element, self.__attribute, self.__value))
        if self.__condition == Condition.EQUAL:
            WebDriverWait(Driver.driver(), timeout=self.__time).until(self.__attribute_to_equal_value(element, self.__attribute, self.__value))

class PresentElement(IWait):
    
    __time = 0
    
    def __init__(self, builder):
        super(PresentElement, self).__init__()
        self.__time = builder.base_time
        if self.__time == 0:
            raise TestException("Time is null. Add the 'forAMaxTimeOf' method.")
        if builder.base_condition != Condition.INVALID_CONDITION:
            raise TestException("Condition is not null. Remove the 'to' method.")
        if builder.base_value is not None:
            raise TestException("Value is not null. Remove the 'value' method.")
        if builder.base_exp_total_count != 0:
            raise TestException("Expected total count is not null. Remove the 'withACountOf' method.")
        if builder.base_attribute is not None:
            raise TestException("Attribute is not null. Remove the 'forAttribute' method.")

    def __present_defined_element(self, element):
        def predicate(driver):
            result = False
            try: element.is_displayed()
            except StaleElementReferenceException:
                result = False
            else:
                result = True
            return result
        return predicate
    
    def on(self, element):
        if hasattr(element, "by"):
            WebDriverWait(Driver.driver(), timeout=self.__time).until(EC.visibility_of_element_located((element.by(), element.locator())))
        else:
            WebDriverWait(Driver.driver(), timeout=self.__time).until(self.__present_defined_element(element))

class PresentElementText(IWait):
    __time = 0
    __condition = Condition.INVALID_CONDITION
    __value = None

    def __init__(self, builder):
        super(PresentElementText, self).__init__()
        self.__time = builder.base_time
        self.__condition = builder.base_condition
        self.__value = builder.base_value
        if self.__time == 0:
            raise TestException("Time is null. Add the 'forAMaxTimeOf' method.")
        if self.__condition == Condition.INVALID_CONDITION:
            raise TestException("Please select a valid condition. Unable to execute because condition is not valid.")
        if self.__value is None:
            raise TestException("Value is null. Add the 'value' method.")
        if builder.base_attribute is not None:
            raise TestException("Attribute is not null. Remove the 'forAttribute' method.")
        if builder.base_exp_total_count != 0:
            raise TestException("Expected total count is not null. Remove the 'withACountOf' method.")
        
    def __text_to_equal_value(self, element, value):
        def predicate(driver):
            result = False
            actual_value = element.text
            if actual_value.lower() == value.lower():
                result = True
            return result
        return predicate
    
    def __text_to_contain_value(self, element, value):
        def predicate(driver):
            result = False
            actual_value = element.text
            if value.lower() in actual_value.lower():
                result = True
            return result
        return predicate
    
    def on(self, element):
        if hasattr(element, "by"):
            element = Commands.get_element(element)
        if self.__condition == Condition.CONTAIN:
            WebDriverWait(Driver.driver(), timeout=self.__time).until(self.__text_to_contain_value(element, self.__value))
        if self.__condition == Condition.EQUAL:
            WebDriverWait(Driver.driver(), timeout=self.__time).until(self.__text_to_equal_value(element, self.__value))                    