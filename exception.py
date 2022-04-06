import os

def error_message_detail(error, error_detail):
    _,_, exc_tb = error_detail.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    error_message = f"Error occurred python script name {file_name} line number {exc_tb.tb_lineno} error message {error}"
    return error_message


class ProjectException(Exception):

    def __init__(self, error_message, error_detail):
        '''
        :param error_message: error message in string format
        '''
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __repr__(self):
        return ProjectException.__name__.__str__()

    def __str__(self):
        return self.error_message

