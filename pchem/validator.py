import pchem.constants 
import pchem.utils

# Validation logic for API arguments. 
# Each validator must return: 
# 1) Boolean value indicating whether the args are valid.
# 2) String description of the validation errors, if any.

def get_version(args):
    return _no_validation()

def get_identity(args):
    return _no_validation()

def open_emulation(args):
    is_valid = pchem.utils.check_file_extension(args["sim_file_path"], ".smu")
    validation_errors = ""
    if not is_valid:
        validation_errors = '"The Propsim simulation file path must have an extension ".sum"'
    return {pchem.constants.IS_VALID_KEY:is_valid, 
            pchem.constants.VALIDATION_ERRORS_KEY:validation_errors}

def edit_emulation(args):
    is_valid = pchem.utils.check_file_extension(args["sim_file_path"], ".sum")
    validation_errors = ""
    if not is_valid:
        validation_errors = '"The Propsim simulation file path must have an extension ".sum"'
    return {pchem.constants.IS_VALID_KEY:is_valid, 
            pchem.constants.VALIDATION_ERRORS_KEY:validation_errors}

def start_emulation(args):
    return _no_validation()

def pop_error_queue(args):
    return _no_validation()

def start_emulation_after_edit(args):
    return _no_validation()

def pause_emulation(args):
    return _no_validation()

def resume_emulation(args):
    return _no_validation()

def close_emulation(args):
    return _no_validation()

def set_channel_gain_imbalance(args):
    return _no_validation()

def set_channel_group_frequency(args):
    return _no_validation()

def set_channel_shadowing(args):
    return _no_validation()

def get_channel_shadowing(args):
    return _no_validation()

def get_channel_shadowing_state(args):
    return _no_validation()

def get_output_gain(args):
    return _no_validation()

def get_input_loss(args):
    return _no_validation()

def set_channel_shadowing_state(args):
    return _no_validation()

def set_input_loss(args):
    is_valid = True
    validation_errors = ""
    # Check Input numbers
    if args["loss"] > 100 or args["loss"] < -100:
        is_valid = False
        validation_errors = "loss must be between -100 and 100 dB"

    return {pchem.constants.IS_VALID_KEY:is_valid, 
            pchem.constants.VALIDATION_ERRORS_KEY:validation_errors}

def set_output_gain(args):
    is_valid = True
    validation_errors = ""
    # Check Output numbers
    if args["gain"] > 0 or args["gain"] < -100:
        is_valid = False
        validation_errors = "output gain must be between -100 and 0 dB"

    return {pchem.constants.IS_VALID_KEY:is_valid, 
            pchem.constants.VALIDATION_ERRORS_KEY:validation_errors}


# def set_channel_frequency(args):
#     is_valid = True
#     validation_errors = ""

def _no_validation():
    is_valid = True
    validation_errors = ""
    return {pchem.constants.IS_VALID_KEY:is_valid, 
            pchem.constants.VALIDATION_ERRORS_KEY:validation_errors}
