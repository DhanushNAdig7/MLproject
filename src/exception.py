import sys
from typing import Tuple

def error_message(error, error_details: sys.exc_info()) -> str:
    """
    Formats an error message to include details about the exception,
    the file name, and the line number where the error occurred.

    Args:
        error: The exception object.
        error_details: The result of sys.exc_info().

    Returns:
        A formatted error message string.
    """
    exc_type, exc_value, exc_tb = error_details
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: str, error_details: sys.exc_info()):
        super().__init__(error_message)
        self.error_details = error_details

    def __str__(self):
        return error_message(self, self.error_details)

if __name__ == "__main__":
    try:
        a = 1 / 0
    except ZeroDivisionError as e:
        custom_exception = CustomException(
            "Division by zero error occurred", sys.exc_info()
        )
        print(custom_exception)

    try:
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError as e:
        custom_exception = CustomException(
            "Index out of bounds error", sys.exc_info()
        )
        print(custom_exception)