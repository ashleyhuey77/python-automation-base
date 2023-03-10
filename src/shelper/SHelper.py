'''
Created on Nov 20, 2018

@author: ashleyhuey
'''
from shelper.base.ClickContext import ClickContext
from shelper.base.EnterContext import EnterContext
from shelper.base.TextContext import TextContext
from shelper.base.ElementContext import ElementContext
from shelper.base.ActionsContext import ActionsContext
from shelper.strat.Click import Click, JSClick, JQClick
from shelper.strat.Element import Element
from shelper.strat.Enter import Enter
from shelper.strat.Browser import Browser
from shelper.strat.Actions import Actions
from shelper.strat.Page import Page
from shelper.base.WaitContext import WaitContext
from shelper.Enums import Wait
from shelper.strat.Text import Text, JSText, AttributeText
from shelper.Enums import Via, Variable
from shelper.base.BrowserContext import BrowserContext
from shelper.base.PageContext import PageContext

class SHelper(object):

    @staticmethod
    def click(via):
        click = None
        if via == Via.SELENIUM:
            click = ClickContext(Click)
        elif via == Via.JAVASCRIPT:
            click = ClickContext(JSClick)
        elif via == Via.JQUERY:
            click = ClickContext(JQClick)
        return click
    
    @staticmethod
    def text(variable, via):
        action = ""
        if via == Via.SELENIUM:
            if variable == Variable.ELEMENT:
                action = TextContext(Text)
            elif variable == Variable.ATTRIBUTE:
                action = TextContext(AttributeText)
        elif via == Via.JAVASCRIPT:
            action = TextContext(JSText)
        return action
    
    @staticmethod
    def enter():
        action = EnterContext(Enter)
        return action
    
    @staticmethod
    def browser():
        action = BrowserContext(Browser)
        return action
    
    @staticmethod
    def element():
        action = ElementContext(Element)
        return action
    
    @staticmethod
    def page():
        action = PageContext(Page)
        return action
    
    @staticmethod
    def actions():
        act = ActionsContext(Actions)
        return act
    
    @staticmethod
    def wait(condition, builder):
        action = None
        if condition == Wait.PRESENCE_OF_ELEMENT:
            action = WaitContext(wait.PresentElement(builder))
        elif condition == Wait.PRESENCE_OF_ELEMENT_TEXT:
            action = WaitContext(wait.PresentElementText(builder))
        elif condition == Wait.ELEMENT_NOT_TO_BE_PRESENT:
            action = WaitContext(wait.NonPresentElement(builder))
        elif condition == Wait.ELEMENT_TEXT_NOT_TO_BE_PRESENT:
            action = WaitContext(wait.NonPresentElementText(builder))
        elif condition == Wait.PRESENCE_OF_ATTRIBUTE:
            action = WaitContext(wait.PresentAttribute(builder))
        elif condition == Wait.PRESENCE_OF_ATTRIBUTE_TEXT:
            action = WaitContext(wait.PresentAttributeText(builder))
        elif condition == Wait.ATTRIBUTE_NOT_TO_BE_PRESENT:
            action = WaitContext(wait.NonPresentAttribute(builder))
        elif condition == Wait.ATTRIBUTE_TEXT_NOT_TO_BE_PRESENT:
            action = WaitContext(wait.NonPresentAttributeText(builder))
        elif condition == Wait.CLICKABILITY_OF_ELEMENT:
            action = WaitContext(wait.ClickableElement(builder))
        elif condition == Wait.COUNT_OF_ELEMENTS:
            action = WaitContext(wait.ElementCount(builder))
        return action
    
import shelper.strat.Wait as wait        
        