import sys
from src.logger import logging

def get_error_message(error_message,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error Occure in Python script name {} line number {} error message {}".format(filename,exc_tb.tb_lineno,str(error_message)) 

    return error_message

class CustomeException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message,error_details=error_details)
        
    def __str__(self):
        return self.error_message