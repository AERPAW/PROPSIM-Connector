from constants import *

def create_pchem_response(status=RESPONSE_STATUS.UNKNOWN, error="", result=""):
    pchem_response = {PCHEM_STATUS_KEY: status, 
                      PCHEM_ERROR_KEY: error,
                      PCHEM_RESULT_KEY: result}
    return pchem_response


def check_file_extension(fpath, required_extension):
    is_extension = fpath.lower().endswith(required_extension)
    return is_extension
