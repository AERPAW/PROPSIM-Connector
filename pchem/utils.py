import constants

def create_error_response(details):
    response = {"status": "error", "details":details}
    return response

def create_ok_response(details):
    response = {"status": "ok", "details":details}
    return response

def create_pchem_response(is_valid, validation_errors, propsim_at_response):
    pchem_response = {constants.IS_VALID_KEY: is_valid, 
                      constants.VALIDATION_ERRORS_KEY: validation_errors,
                      constants.EXECUTION_RESULT_KEY: propsim_at_response}
    return pchem_response