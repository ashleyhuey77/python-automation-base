'''
Created on Nov 28, 2018

@author: ashleyhuey
'''
from enum import Enum

class ReportType(Enum):

    TEST_RESULTS_REPORT = 1
   
class Status(Enum):
    
    FAIL = 1
    WARNING = 2
    PASS = 3
    SCREENSHOT = 4
    DONE = 5
    DEBUG = 6