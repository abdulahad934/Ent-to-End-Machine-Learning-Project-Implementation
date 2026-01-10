import sys

def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return str(error)

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{line_number}] "
        f"error message [{error}]"
    )


class USvisaException(Exception):
    def __init__(self, error_message, error_detail):
        self.error_message = error_message_detail(
            error_message, error_detail
        )
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message
