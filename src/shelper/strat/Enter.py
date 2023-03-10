'''
Created on Nov 26, 2018

@author: ashleyhuey
'''
from shelper.base.EnterContext import IEnter
from shelper.abst.Commands import Commands

class Enter(IEnter):

    def text_into(self, element, text):
        if hasattr(element, "by"):
            Commands.get_element(element).send_keys(text)
        else:
            element.send_keys(text)
            
    def clear(self, element):
        if hasattr(element, "by"):
            Commands.get_element(element).clear()
        else:
            element.clear()
        