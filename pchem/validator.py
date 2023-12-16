import constants 
import utils

# Validation logic for API arguments. 
# Each validator must return: 
# 1) Boolean value indicating whether the args are valid.
# 2) String description of the validation errors, if any.

def get_version(args):
    return _no_validation()

def get_identity(args):
    return _no_validation()

def open_emulation(args):
    is_valid = utils.check_file_extension(args["sim_file_path"], ".sum")
    validation_errors = ""
    if not is_valid:
        validation_errors = '"The Propsim simulation file path must have an extension ".sum"'
    return {constants.IS_VALID_KEY:is_valid, 
            constants.VALIDATION_ERRORS_KEY:validation_errors}

def edit_emulation(args):
    is_valid = utils.check_file_extension(args["sim_file_path"], ".sum")
    validation_errors = ""
    if not is_valid:
        validation_errors = '"The Propsim simulation file path must have an extension ".sum"'
    return {constants.IS_VALID_KEY:is_valid, 
            constants.VALIDATION_ERRORS_KEY:validation_errors}

def start_emulation(args):
    return _no_validation()

def start_emulation_after_edit(args):
    return _no_validation()

def pause_emulation(args):
    return _no_validation()

def resume_emulation(args):
    return _no_validation()

def close_emulation(args):
    return _no_validation()

# def set_input_state(args):
#     return _no_validation()

# def set_output_state(args):
#     is_valid = True
#     validation_errors = ""

# def set_input_gain(args):
#     is_valid = True
#     validation_errors = ""

# def set_input_loss(args):
#     is_valid = True
#     validation_errors = ""

# def set_channel_frequency(args):
#     is_valid = True
#     validation_errors = ""

def _no_validation():
    is_valid = True
    validation_errors = ""
    return {constants.IS_VALID_KEY:is_valid, 
            constants.VALIDATION_ERRORS_KEY:validation_errors}
